import discord, asyncio, datetime
from haversine import calculate_haversine

DURATION_TILL_TIMEOUT = datetime.timedelta(minutes=15)

async def scrollmenu(bot, cmd_context, retriever):
    json_events = retriever.get_events_data()
    events_sig = json_events['data']

    if not events_sig:
        await cmd_context.send(embed=format_embed())
        return
        
    page_data = json_events['meta']
    current_page = 0
    last_page = page_data['to']-1
    total_events = page_data['total']

    grade_level = events_sig[current_page]['program']['code']

    if (grade_level == 'V5RC'):
        message = await cmd_context.send(embed=format_embed(current_page+1, total_events, events_sig[current_page]))
        await add_scroll_menu(message, current_page, last_page)

        while (retriever.cur_time - message.created_at) < DURATION_TILL_TIMEOUT:
            valid_reactions = ['⬅️', '➡️', '⏪', '⏩']
            
            def check(reaction, user):
                return user == cmd_context.author and reaction.emoji in valid_reactions and message == reaction.message

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=5, check=check)
                if reaction.emoji == '⬅️':
                    current_page-=1
                    await message.edit(embed=format_embed(current_page+1, total_events, events_sig[current_page]))
                    await message.clear_reactions()
                    await add_scroll_menu(message, current_page, last_page)
                elif reaction.emoji == '➡️':
                    current_page+=1
                    await message.edit(embed=format_embed(current_page+1, total_events, events_sig[current_page]))
                    await message.clear_reactions()
                    await add_scroll_menu(message, current_page, last_page)
                elif reaction.emoji == '⏪':
                    current_page = 0
                    await message.edit(embed=format_embed(current_page+1, total_events, events_sig[current_page]))
                    await message.clear_reactions()
                    await add_scroll_menu(message, current_page, last_page)
                elif reaction.emoji == '⏩':
                    current_page = last_page
                    await message.edit(embed=format_embed(current_page+1, total_events, events_sig[current_page]))
                    await message.clear_reactions()
                    await add_scroll_menu(message, current_page, last_page)

            except asyncio.TimeoutError:
                pass

            retriever.update_current_time()

def format_embed(current_page=-1, last_page=-1, event=None):
    if event is None:
        embed = discord.Embed(
            description = 'No events were found :(',
            color = discord.Color.orange(), 
            title = 'Oops....'
        )
    else:
        embed = discord.Embed(
            color = discord.Color.green(),
            description = f'''
            Date: {event['start']}\n
            Location: {event['location']['venue']}\n
            Address: {event['location']['address_1']}, {event['location']['city']}, {event['location']['region']}, {event['location']['country']}\n
            Approximate distance from Austin: {calculate_haversine(event['location']['coordinates']['lat'], event['location']['coordinates']['lon']):.2f} miles
            ''',
            title = event['name'],
            url = f'https://www.robotevents.com/robot-competitions/vex-robotics-competition/{event['sku']}.html#general-info'
        )
        embed.set_footer(text=f'Page {current_page} of {last_page}')
    return embed

async def add_scroll_menu(msg, current_page, last_page):
    if msg.embeds[0].url:
        if (current_page != 0):
            await msg.add_reaction('⏪')
            await msg.add_reaction('⬅️')
        if (current_page != last_page):
            await msg.add_reaction('➡️')
            await msg.add_reaction('⏩')