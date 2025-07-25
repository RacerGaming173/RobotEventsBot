import discord, scraper, vars

intents = discord.Intents.none()
intents.message_content = True
intents.messages = True
intents.reactions = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!locals'):
        events_retriever = scraper.RetrieveEventData()
        events_retriever.set_query_param('region', 'Texas - Region 4')
        json_events_local = events_retriever.get_events_data()
        events_local = json_events_local['data']

        if not events_local:
            await message.channel.send('empty')

        for loc_event in events_local:
            grade_level = loc_event['program']['code']

            if (grade_level == 'V5RC'):
                await message.channel.send(embed=format_embed(loc_event))

    if message.content.startswith('!sigs'):
        events_retriever = scraper.RetrieveEventData()
        events_retriever.clear_query_param('region')
        events_retriever.set_query_param('level', 'Signature')
        json_events_sig = events_retriever.get_events_data()
        events_sig = json_events_sig['data']

        if not events_sig:
            await message.channel.send('empty')

        for sig_event in events_sig:
            grade_level = sig_event['program']['code']

            if (grade_level == 'V5RC'):
                await message.channel.send(embed=format_embed(sig_event))

def format_embed(event):
    embed = discord.Embed(
        title = event['name'], 
        description=f'''
        Date: {event['start']}\n
        Location: {event['location']['venue']}\n
        Address: {event['location']['address_1']}, {event['location']['city']}, {event['location']['region']}, {event['location']['country']}
        ''',
        url = f'https://www.robotevents.com/robot-competitions/vex-robotics-competition/{event['sku']}.html#general-info'
    )
    return embed

client.run(vars.discord_api_key)