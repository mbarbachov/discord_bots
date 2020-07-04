import discord

TOKEN = 'NzI4Nzk4Mjk4OTQwMzc1MTMw.Xv_obQ.8xdR82eoWWRGwg2HLtyZJdChZPw'

client = discord.Client()
INITIATED = False


@client.event
async def on_ready():
    print('------------')
    print(f'USERNAME: {client.user.name}')
    print(f'USER-ID : {client.user.id}')
    print('------------')


@client.event
async def on_member_join(member):
    INITIATED = True


@client.event
async def on_message(message):
    pass


client.run(TOKEN)
