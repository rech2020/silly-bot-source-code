import disnake
from disnake.ext import commands
import os
import time
import subprocess
import sys
import random
from random import *
from glibberisher import *
from gibberish import Gibberish
intents = disnake.Intents.all()

gib = Gibberish()

bot = commands.Bot(command_prefix="ba!", reload=True, intents=intents)

# people ids
hexahedron1 = 801078409076670494
tema5002 = 558979299177136164
ammeter = 811569586675515433
rech2020 = 710621353128099901
slinx92 = 903650492754845728
kesslon = 1143072932596305932
d = 1143072932596305932
# bad people ids 
goober = 691598832273850440
iforgotwhoisthat = 795404576839958529
roll_cake = 318571303881801728
tintin = 735971349973172355
# trusteds list
trusteds = [hexahedron1, tema5002, slinx92, rech2020, kesslon, d]
# retards list
retards = [goober, iforgotwhoisthat, roll_cake, tintin]
# servers
barhtolomew_server = 1195939785928364132

async def status_resync():
    print("resyncing presence")
    people = 0
    for every in bot.guilds:
        people += every.member_count
        print(f"{people} people... ({every.member_count} people from {every.name})")
    await bot.change_presence(
        status=disnake.Status.online,
        activity=disnake.Game(f"with {people} people on {len(bot.guilds)} servers"),
    )
    print("presence changed\n-----")

@bot.event
async def on_ready():
    channel = bot.get_channel(1197770600178003981)
    slinx_channel = bot.get_channel(1042064947867287646)
    randomnum = randint(1, 4)
    print("Powerup inniciated.")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")
    print("setting presence")
    people = 0
    for every in bot.guilds:
        people += every.member_count
        print(f"{people} people... ({every.member_count} people from {every.name})")
    await bot.change_presence(
        status=disnake.Status.online,
        activity=disnake.Game(f"with {people} people on {len(bot.guilds)} servers"),
    )
    print("presence changed\n-----")
    try: await channel.send("hello gordon")
    except: print('somehow failed to send message?????')
    if randomnum == 1:
        try: await slinx_channel.send("i have been started or reloaded") # TODO add some wake up quotes
        except: print('somehow failed to send message????')

#@bot.event
#async def on_message(message):
#    if message == "hey bartholomew kys":
#        if message.author.id == rech2020:
#            await message.channel.send(file=disnake.File("metal_pipe_falling_sound.mp3"))
#            print("i am dead")
#            time.sleep(1)
#            exit()
#        else:
#            await message.channel.send("nuh uh")
#            print(f"{message.author.name} tried to kill me but failed due to perms issue")

@bot.event
async def on_guild_remove(guild):
    channel = bot.get_channel(1195947266855403590)
    try:
        await channel.send(
            f"**{guild.owner.name}** пидорас тупой он меня по IP забанил с сервера **{guild.name}** :hugging::hugging::hugging::smiling_face_with_3_hearts::smiling_face_with_3_hearts::exploding_head::relaxed::relaxed::relaxed::kissing_heart::kissing_heart::kissing_heart::heart_eyes::heart_eyes::blush::blush::kissing_closed_eyes::kissing_closed_eyes:"
        )
    except:
        await channel.send(
            "i got removed from some server which name i dont know or failed to fetch"
        )


@bot.event
async def on_member_join(member):
    print(
        f"{member.name}(user with id {member.id}) joined the {member.guild.name} server aka server with id {member.guild.id}"
    )
    if member.id in retards:
        print("wait a second... is that... is that that one person from the retards list!?")
        print("you know what i am going to ban that person")
        print("attempting to ban that person...")
        try:
            await member.guild.ban(member.id, delete_message_days=0, reason='is in retards list')
        except:
            print("i failed to ban that person, time for plan B")
            role = barhtolomew_server.get_role(1195957915916447744)
            print(f"attempting to add role {role.name} to {member.name}")
            try: await member.add_roles(role)
            except:
                print(f"i have failed to add role {role.name} to {member.name}")
                moderator_only = bot.get_channel(1195940341438746714)
                await moderator_only.send(f"hello <@&1195946019351973888> HELP\n<@{member.id}> HAS GOT PAST BOTH DEFENCES\nSOMEBODY BAN THIS PERSON")
    elif member.guild.id == 1195939785928364132:
        print(f"as you know by now that person joined the barhtolomew server if i put the id right")
        if member.id not in trusteds:
            role = barhtolomew_server.get_role(1199173994654486738)
            print(f"attempting to add role {role.name} to {member.name}")
            try: await member.add_roles(role)
            except: print(f'i failed to add role {role.name} to {member.name}')
    await status_resync()


@bot.user_command()
async def avatar(inter, user):
    embed = disnake.Embed(title=str(user))
    embed.set_image(url=user.display_avatar.url)
    await inter.response.send_message(embed=embed)


@bot.command(name="helpp")
async def helpp(ctx):
    if ctx.author.id in retards:
        await ctx.send("no i will not help you")
    else:
        await ctx.send("this is not implemented yet <:typing:1195957954193653990>")
        await ctx.send("anyways \n https://discord.com/invite/CADYGFuYcc")


@bot.slash_command(name="buttons", description="testing buttons")
async def buttons(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(
        "test",
        components=[
            disnake.ui.Button(
                label="testing testing 1 2 3",
                style=disnake.ButtonStyle.success,
                custom_id="success",
            ),
            disnake.ui.Button(
                label="danger button",
                style=disnake.ButtonStyle.danger,
                custom_id="danger",
            ),
        ],
    )


@bot.listen("on_button_click")
async def buttons_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["success", "danger"]:
        return

    if inter.component.custom_id == "success":
        await inter.response.send_message("test success")
    elif inter.component.custom_id == "danger":
        await inter.response.send_message("do not press the danger button")


@bot.slash_command(name="server_info", description="get server info or something")
async def server_info(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(
        f"Server name: {inter.guild.name}\nTotal members: {inter.guild.member_count}"
    )


@bot.slash_command(name="say", description="talk as a bot")
async def say(ctx, text: str, guild_id: str = None, channel_id: str = None):
    if guild_id is None:
        guild_id = ctx.guild.id
    else:
        try:
            guild_id = int(guild_id)
        except:
            await ctx.send("invalid guild id", ephemeral=True)
            return
    if channel_id is None:
        channel_id = ctx.channel.id
    else:
        try:
            channel_id = int(channel_id)
        except:
            await ctx.send("invalid channel id", ephemeral=True)
            return
    if ctx.author.id in trusteds or ctx.author.id == ctx.guild.owner_id:
        await ctx.send("ok", ephemeral=True)
        guild = bot.get_guild(guild_id)
        channel = guild.get_channel(channel_id)
        try:
            await channel.send(text)
            print(f"{ctx.author.name}({ctx.author.id}) used /say to say in {guild.name} #{channel.name}\n{text}")
        except:
            try: print(f'i failed to send the message("{text}") in {channel.name} maybe because i am missing permissions\n anyways {ctx.author.name} asked me to send that message')
            except: print(f'i failed to send the message ("{text}") in {ctx.channel.name} maybe because i am missing permissions\n anyways {ctx.author.name} asked me to send that message')
    else:
        await ctx.send("nuh uh", ephemeral=True)


@bot.slash_command(name="guild_info", description="get info about a guild aka server")
async def guild_info(inter, guild_id):
    try: guild_id = int(guild_id)
    except:
        await inter.response.send_message('not an id <:typing:1195957954193653990>')
        return
    guild = bot.get_guild(guild_id)
    if guild is None:
        await inter.response.send_message("Guild not found.")
        return

    message = f"Guild Name: {guild.name}\n"
    message += f"Guild ID: {guild.id}\n"
    message += f"Owner: {guild.owner.name}\n"
    message += f"Owner ID: {guild.owner_id}\n"
    message += f"Text channels: {len(guild.text_channels)}\n"
    message += f"Member Count: {guild.member_count}\n"
    print(message)
    await inter.response.send_message(message)


@bot.slash_command(name="user_info", description="get some info about your account")
async def user_info(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(
        f"Your tag: {inter.author}\nYour ID: {inter.author.id}"
    )


@bot.slash_command(name="msg_console", description="send a message to rech2020's console")
async def msg_console(ctx, msg):
    print(f"um hello {ctx.author.name} left a message fo you: {msg}")
    await ctx.send("done", ephemeral=True)

@bot.slash_command(name='servers_list', description='get list of servers bot is in')
async def servers_list(ctx):
    if ctx.author.id in trusteds:
        message = ''
        for guild in bot.guilds:
            message += f"Guild Name: {guild.name}\n"
            message += f"Guild ID: {guild.id}\n"
            message += f"Owner ID: {guild.owner_id}\n"
            message += f"Owner: {bot.get_user(guild.owner_id)}\n"
            message += f"Text channels: {len(guild.text_channels)}\n"
            message += f"Member Count: {guild.member_count}\n\n"
        try: await ctx.send('```' + message + '```', ephemeral=True)
        except: await ctx.send('message got too long')
    else:
        await ctx.send('perms issue')

@bot.slash_command(name='channel_list', description='get list  of channels of a server that bot is in')
async def channel_list(ctx, guild_id):
    try: guild_id = int(guild_id)
    except:
        await ctx.send('not an id <:typing:1195957954193653990>')
        return
    guild = bot.get_guild(guild_id)
    if guild is None:
        await ctx.send('invalid guild id or failed to get guild')
        return
    channel_list = guild.channels
    message = f"{guild.name}'s channels\n"
    for channel in channel_list:
        try: message += f"Channel name: {channel.name}\n"
        except: message += f"Channel name: i failed to fetch\n"
        try: message += f"Channel description: {channel.description}\n"
        except: message += f"Channel description: none or i failed to fetch\n"
        try: message += f"Channel type: {channel.type}\n"
        except: message += "Channel type: failed to fetch\n"
        try: message += f"Channel ID: {channel.id}\n"
        except: message += "Channel ID: somehow failed to fetch???\n"
        try: message += f"Channel category name: {channel.category.name}\n"
        except: message += "Channel category name: None\n"
        message += "\n"
    print(message)
    await ctx.send('```' + message + '```', ephemeral=True)

@bot.command(name="emojis")
async def emojis(ctx):
    if ctx.author.id in trusteds:
        message = ""
        for guild in bot.guilds:
            message = f"{guild.name}'s emojis:\n"
            for emoji in guild.emojis:
                animated = emoji.animated
                message += "<"
                if animated:
                    message += "a"
                message += f":{emoji.name}:{emoji.id}>"
            try: await ctx.send(message)
            except: await ctx.send(f'failed to send message because {guild.name} has too many emojis🎉🎉🎉🎉🎉🎉🎉🎉')
    else:
        await ctx.send('this is ~~not~~ implemented yet <:typing:1195957954193653990>')

@bot.command(name='inviter', description='attempt to create invite to a guild')
async def inviter(ctx, guild_id):
    if ctx.author.id in trusteds:
        try: guild_id = int(guild_id)
        except:
            await ctx.send('not an id <:typing:1195957954193653990>')
            return
        guild = bot.get_guild(guild_id)
        try: permissions = guild.me.guild_permissions
        except: await ctx.send('i am not in that server <:typing:1195957954193653990>')
        if guild is None:
            await ctx.send('invalid guild id or failed to get guild')
            return
        channel_list = guild.text_channels
        if permissions.create_instant_invite:
            for channel in channel_list:
                invite = await channel.create_invite()
                try: await ctx.send(f"{invite.url}")
                except: await ctx.send(f"i failed to send invite🎉🎉🎉🎉🎉🎉🎉🎉")
        else:
            await ctx.send("i don't have permission to make invite in that server🎉🎉🎉🎉🎉🎉🎉")
    else:
        await ctx.send("perms issue")

@bot.command(name='gibberish')
async def gibberisher(ctx):
    await ctx.send("this is not implemented yet <:typing:1195957954193653990>")

@bot.command(name='glibberish')
async def glibberish(ctx: disnake.MessageInteraction):
    await ctx.send(
        "choose type of glibberish",
        components=[
            disnake.ui.Button(
                label="word",
                style=disnake.ButtonStyle.secondary,
                custom_id="word",
            ),
            disnake.ui.Button(
                label="sentence",
                style=disnake.ButtonStyle.secondary,
                custom_id="sentence",
            ),
            disnake.ui.Button(
                label="text",
                style=disnake.ButtonStyle.secondary,
                custom_id="text",
            ),
        ],
    )

@bot.listen("on_button_click")
async def help_listener(ctx: disnake.MessageInteraction):
    if ctx.component.custom_id not in ["word", "sentence", "text"]:
        return

    if ctx.component.custom_id == "word":
        await ctx.send(f"here's your glibberish word: {gen_word()}")
    elif ctx.component.custom_id == "sentence":
        await ctx.send(f"here's your glibberish sentence: {gen_sentence()}")
    elif ctx.component.custom_id == "text":
        await ctx.send(f"here's a glibberish text:\n```\n{gen_text()}\n```")

@bot.command(name="die")
async def die(ctx):
    if ctx.author.id in trusteds:
        await ctx.send(file=disnake.File("metal_pipe_falling_sound.mp3"))
        print("i am dead")
        time.sleep(1)
        exit()
    else:
        await ctx.send("nuh uh")
        print(f"{ctx.author.name} tried to kill me but failed due to perms issue")

@bot.command(name='reload')
async def reload(ctx):
    await ctx.send('ok wait')
    subprocess.Popen(['python', 'main.py'])
    sys.exit(0)

bot.load_extension("cogs.ping")

bot.run(open("token.txt").read())
