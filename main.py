import discord, scrollmenu, scraper, vars
from discord.ext import commands

intents = discord.Intents.none()
intents.message_content = True
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

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

bot.run(vars.DISCORD_API_KEY)