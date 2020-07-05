import discord
import random
import asyncio

TOKEN = 'NzI4Njg1MjU0MjMxMTk1Njg4.XwCiOw.0puJ-S_zHXvIPNFkE9UneceyTl8'

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

global tag
tag = '!'


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    global tag

    if message.author == client.user:
        return

    if message.content.startswith(f'{tag}hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith(f'{tag}goodbye'):
        msg = 'Goodbye {0.author.mention}'.format(message)
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith(f'{tag}f'):
        msg = f'**F U** {message.author.mention} \n {random.choice(l_database)}'
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith(f'{tag}e'):
        for i in range(5):
            await message.channel.send('e')

    if message.content.startswith(f'{tag}***E***'):
        for i in range(5):
            await message.channel.send('***E E E E E***')

    if message.content.startswith(f'{tag}helpimdead') or message.content.startswith('!help im dead'):
        msg = 'Lol sucks to be {0.author.mention}'.format(message)
        print(msg)
        await message.channel.send(msg)

    if message.content.startswith(f'{tag}meme'):
        await message.channel.send(random.choice(list_o_memes))

    if message.content.startswith(f'{tag}moji'):
        await message.channel.send(':stalinapple: !')
        png_file = open('images/Michelle_shared_a_sketch_with_you.png', 'r')
        await message.channel.send(png_file)

    if message.content.startswith(f'{tag}ch-tag'):
        # check perms (in dev)
        m = message.content
        print(message.content[len(tag) + 7:])
        if len(message.content[len(tag) + 7:]) > 0:
            # there is a given tag
            tag = message.content[len(tag) + 7:]

        await message.channel.send(f'Command tag set to: {tag}')


client.run(TOKEN)
