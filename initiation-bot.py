import discord
import time

TOKEN = 'NzI4Nzk4Mjk4OTQwMzc1MTMw.XwCjSw.8u5OTo99S4R7GJld05YItk2GyJQ'

client = discord.Client()

people_to_initiate = []
guild_roles = []
commands = dict({})


@client.event
async def on_ready():
    print('------------')
    print(f'USERNAME: {client.user.name}')
    print(f'USER-ID : {client.user.id}')
    print('------------')
    global guild_roles, commands

    print(client.guilds)

    for role in client.guilds[0].roles:
        if str(role) in ['gamer', 'Bread persona', "Don't touch me!", "Le artists", "The alchemist", "kLicitY CLacK"]:
            # acceptable beginner role
            guild_roles.append(role)
            # create a command for that role
            command = f'!{"".join([letter.lower() for letter in role.name if letter.isalpha()])}'
            commands[command] = role

    commands['!mortal'] = None
    print(guild_roles)
    print(commands)


@client.event
async def on_member_join(member):
    time.sleep(0.5)

    # for debugging
    for_debug = member

    # get the two channels that we need to mention
    main_channel = client.get_channel(728338777852084327)
    abilities_channel = client.get_channel(728654620523757638)

    # print information about the guild channels
    print(for_debug.guild.channels)
    print(main_channel)

    # print information about initiation
    await main_channel.send(f'Welcome to the server {member.mention}! '
                            f'Thank you for coming. To start we must initiate you into a class.')
    await main_channel.send(f'Please head over to the channel {abilities_channel.mention} and browse the abilities and '
                            f'choose a class that suits you. After you have done that please come back to '
                            f'{main_channel.mention} and type the command: **!start-initiation**')

    # for debugging purposes
    global people_to_initiate

    people_to_initiate.append(member)


@client.event
async def on_message(message):
    # check if it is the !start-initiation tag
    global commands, people_to_initiate

    if message.content.startswith('!start-initiation'):
        if client.get_channel(728338777852084327) == message.channel:
            print('Correct channel')
            if message.author in people_to_initiate:
                m = 'Starting initiation.'

                await message.channel.send(m)
                time.sleep(0.5)
                msg = ""
                count = 0

                for role in guild_roles:
                    c = f'!{"".join([letter.lower() for letter in role.name if letter.isalpha()])}'
                    # command -> str(role).split()
                    msg += f'If you wish to join {role.mention} type the command: **{c}** \n'
                    count += 1

                msg += f'If you wish to remain mortal type the command: **!mortal**\n'

                await message.channel.send(msg)
            else:
                await message.channel.send(f"I'm sorry {message.author.mention}, but you can't execute this command "
                                           f"because you have already completed initiation.")
        else:
            await message.channel.send(f'You cannot commence initiation in {message.channel.mention}. '
                                       f'Please go to {client.get_channel(728338777852084327).mention} and complete '
                                       f'the command there.')

    if message.content in commands:
        # if a person
        # assign role and finish initiation
        if message.author in people_to_initiate:
            if message.content.startswith('!mortal'):
                # remain mortal
                # everyone = client.get_guild()
                # print(everyone)
                await message.channel.send(f'{message.author.mention} has chosen to remain mortal and '
                                           f'has not ascended.')
            else:
                await message.channel.send(f'{message.author.mention} has chosen to become a '
                                           f'{commands[message.content]} and has ascended to '
                                           f'{commands[message.content].mention}.')
                await message.author.add_roles(commands[message.content])

            # we allow the initiation to commence
            # delete the user from people who can initiate
            people_to_initiate.pop(people_to_initiate.index(message.author))
            await message.channel.send(f'Congratulations {message.author.mention} you are now officially part of the '
                                       f'server!')
        else:
            # we reject the initiation command
            await message.channel.send(f"{message.author.mention} you can"
                                       f"'t change your class. The only way you can do that is to ask one of the mods.")


client.run(TOKEN)
