import discord
import random
import asyncio

TOKEN = 'NzI4Njg1MjU0MjMxMTk1Njg4.Xv-REg.1yfSoNusx6XJ5-6xBjb6E9UFRcA'

client = discord.Client()

l_database = [
    'https://tenor.com/view/flipping-off-flip-off-middle-finger-smile-happy-gif-4746862',
    'https://tenor.com/view/middlefinger-mood-screwyou-leave-me-gif-10174031',
    'https://tenor.com/view/hand-gun-middle-finger-me-to-my-hater-gif-4870509'
]

f = open('meme_links.txt', 'r')
list_o_memes = [line.strip() for line in f]
print(list_o_memes)
f.close()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith('!goodbye'):
        msg = 'Goodbye {0.author.mention}'.format(message)
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith('!f'):
        msg = f'**F U** {message.author.mention} \n {random.choice(l_database)}'
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith('!e'):
        for i in range(5):
            await message.channel.send('e')

    if message.content.startswith('!***E***'):
        for i in range(5):
            await message.channel.send('***E E E E E***')

    if message.content.startswith('!helpimdead') or message.content.startswith('!help im dead'):
        msg = 'Lol sucks to be {0.author.mention}'.format(message)
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith('!meme'):
        await message.channel.send(random.choice(list_o_memes))


client.run(TOKEN)
