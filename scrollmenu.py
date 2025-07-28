import discord, asyncio, vars

async def scrollmenu(bot, cmd_context, retriever):
    json_events = retriever.get_events_data()
    events_sig = json_events['data']

    if not events_sig:
        await cmd_context.send('empty')
        return
    
    page_data = json_events['meta']
    current_page = 0
    last_page = page_data['to']-1
    total_events = page_data['total']

    grade_level = events_sig[current_page]['program']['code']

    if (grade_level == 'V5RC'): # FIX
        message = await cmd_context.send(embed=format_embed(current_page+1, total_events, events_sig[current_page]))
        await add_scroll_menu(message, current_page, last_page)

        while (retriever.cur_time - message.created_at) < vars.DURATION_TILL_TIMEOUT:

            def check(reaction, user):
                return user == cmd_context.author and (reaction.emoji == '⬅️' or reaction.emoji == '➡️')

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=5, check=check)
                #await cmd_context.send(f'{grade_level}, {events_sig[current_page]['name']}')
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

            except asyncio.TimeoutError:
                pass

            retriever.update_current_time()
        await cmd_context.send("15 mins elapsed") # Temp

def format_embed(current_page, last_page, event=None):
    if event is None:
        embed = discord.Embed(
            description = 'No events were found :(',
            color = discord.Color.red(), 
            title = 'Oops....'
        )
    else:
        embed = discord.Embed(
            color = discord.Color.green(),
            description = f'''
            Date: {event['start']}\n
            Location: {event['location']['venue']}\n
            Address: {event['location']['address_1']}, {event['location']['city']}, {event['location']['region']}, {event['location']['country']}
            ''',
            title = event['name'],
            url = f'https://www.robotevents.com/robot-competitions/vex-robotics-competition/{event['sku']}.html#general-info'
        )
        embed.set_footer(text=f'Page {current_page} of {last_page}')
    return embed

async def add_scroll_menu(msg, current_page, last_page):
    if msg.embeds[0].url:
        if (current_page != 0):
            await msg.add_reaction('⬅️')
        if (current_page != last_page):
            await msg.add_reaction('➡️')