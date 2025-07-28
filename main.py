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