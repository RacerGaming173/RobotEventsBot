import discord, threading, scrollmenu, scraper, vars
from flask import Flask
from discord.ext import commands

DISCORD_API_KEY = vars.DISCORD_API_KEY

intents = discord.Intents.none()
intents.message_content = True
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
                description = 'Invalid command',
                color = discord.Color.red(), 
                title = 'Uh oh...'
            )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
                description = 'Missing argument',
                color = discord.Color.red(), 
                title = 'Uh oh...'
            )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
                description = 'An error occurred while trying to process command',
                color = discord.Color.red(), 
                title = 'Uh oh...'
            )
        await ctx.send(embed=embed)

@bot.command()
async def locals(ctx):
    events_retriever = scraper.RetrieveEventData()
    events_retriever.set_query_param('region', 'Texas - Region 4')

    await scrollmenu.scrollmenu(bot, ctx, events_retriever)

@bot.command()
async def sigs(ctx):
    events_retriever = scraper.RetrieveEventData()
    events_retriever.set_query_param('level', 'Signature')

    await scrollmenu.scrollmenu(bot, ctx, events_retriever)

@bot.command()
async def help(ctx):
    embed = discord.Embed(
                description = f'''!locals: Queries list of events in Texas Region 4\n
                                  !sigs: Queries list of signature events\n
                                  ''',
                title = 'Commands List'
            )
    await ctx.send(embed=embed)

# Configure bot to listen on port 8080
app = Flask('__name__')

@app.route('/')
def health_check(request):
    return 'OK'

@app.before_first_request
def start_bot_on_gcr():
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start(target=run_bot)

def run_bot():
    if DISCORD_API_KEY:
        print("Discord token successfully loaded")
        bot.run(DISCORD_API_KEY)
    else:
        print("Discord token not loaded")


def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    bot.run(DISCORD_API_KEY)