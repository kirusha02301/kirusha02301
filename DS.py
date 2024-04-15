import discord

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("да"):
        await message.channel.send('Пизда')
    elif message.content.startswith('Да'):
        await message.channel.send('Пизда')
    elif message.content.startswith('Нет'):
        await message.channel.send('Еблет')
    elif message.content.startswith('А'):
        await message.channel.send('Пошел нахуй')
    elif message.content.startswith('а'):
        await message.channel.send('Пошел нахуй')
    elif message.content.startswith('Че'):
        await message.channel.send('хуй через плечо не горячо если горячо переложи на другое плечо')
    elif message.content.startswith('спасибо'):
        await message.channel.send('за спасибо ебут красиво')
    elif message.content.startswith('Спасибо'):
        await message.channel.send('за спасибо ебут красиво')
    elif message.content.startswith('нахуй'):
        await message.channel.send('Сам иди')
    elif message.content.startswith('кто'):
        await message.channel.send('хуйло')
    elif message.content.startswith('заеб'):
        await message.channel.send('закрой свой рот')
    elif message.content.startswith('кв'):
        await message.channel.send('отьебись со своим кв')
    elif message.content.startswith('@everyone'):
        await message.channel.send('Заебал, не пингуй, сука')
    elif message.content.startswith('Еблан'):
        await message.channel.send('Звали пидоры?')
    elif message.content.startswith('eблан'):
        await message.channel.send('Звали пидоры?')
    elif message.content.startswith('Ладно'):
        await message.channel.send('Хую прохладно')
    elif message.content.startswith('ладно'):
        await message.channel.send('Хую прохладно')

client.run(
    'MTAwMzk3NTI3NTYyNjkwOTc1Nw.Godmoa.jRXvPeCgG6-DCoy_O8G6OpNaGakT-XkihRvK4A')