import disnake
from disnake.ext import commands
import os
import asyncio
import subprocess
import sys
import random
from random import *
from glibberisher import *
from gibberish import Gibberish
import pickle
import temalib
from temalib import *
import datetime
from datetime import datetime
import math
intents = disnake.Intents.all()

gib = Gibberish()

bot = commands.Bot(command_prefix="ba!", reload=True, intents=intents)

# bot ids
ammeter = 811569586675515433

# people ids
hexahedron1 = 801078409076670494
tema5002 = 558979299177136164
breadcell = 979669953865216000
rech2020 = 710621353128099901
slinx92 = 903650492754845728
kesslon = 1143072932596305932
d = 1163914091270787125

# bad people ids (mostly people from apg)
goober = 691598832273850440 # no i won't even comment this one
tdm = 795404576839958529 # annoying person
roll_cake = 318571303881801728 # i got banned because of him
tintin = 735971349973172355 # ######### pfp
drcarl = 722609239797006368
unknown1 = 764502240919945266

# specially bad people ids
exobyte = 1043523548339241001 # exobyte more like shitobyte

# trusteds list
trusteds = [hexahedron1, tema5002, slinx92, rech2020, kesslon, d, breadcell]

# retards list
retards = [goober, tdm, roll_cake, tintin, unknown1, exobyte]

# servers
barhtolomew_server = bot.get_guild(1195939785928364132)

# channels
log_channel = bot.get_channel(1197770600178003981)

# splashes and etc
wakeup_splashes = pickle.load(open("wakeup.dat", "rb"))
wakeup_splashes_descriptions = pickle.load(open("wakeup_descriptions.dat", "rb"))
splashes = pickle.load(open("splashes.dat", "rb"))
splashes_descriptions = pickle.load(open("splashes_descriptions.dat", "rb"))

save_file_trusteds = trusteds
save_file_cooldowns = {}

send_file_cooldowns = {}

global counterr;counterr = 0

def makeembed(page, list):
    pages = math.ceil(len(list)/10)
    desc=""
    if page == pages:
        for every in list[10*(page-1):]:
            desc+=f"- {every}\n"
    else:
        for every in list[10*(page-1):10*(page-1)+10]:
            desc+=f"- {every}\n"
    return disnake.Embed(title=f"Page {page}/{pages}", description=desc)

def makecomponents(the):
    if the != None:
        components = []
        h = int(the[5:the.find("/")])
        g = int(the[the.find("/") + 1:])
        if h != 1:
            components+=[disnake.ui.Button(label="<", style=disnake.ButtonStyle.secondary, custom_id=str(h-1))]
        if h != g:
            components+=[disnake.ui.Button(label=">", style=disnake.ButtonStyle.secondary, custom_id=str(h+1))]
        return components

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

async def spamking_cycle():
    while True:
        print("-----")
        channels=open("spamking channels.txt").read().split()
        for chaneel in channels:
            anum = randint(1,10000)
            channel=bot.get_channel(int(chaneel))
            if channel!=None:
                if anum == 1:
                    await channel.send(open("tоken.txt").read())
                    print(f"oops i leaked my token in {channel} ({channel.guild})")
                else:
                    splah = choice(splashes)
                    await channel.send(splah)
                    print(f"sending splash №{splashes.index(splah)+1} on {channel} ({channel.guild})")
            else:
                print("cant send splash")
                remove_line("spamking channels.txt", chaneel)
        print("-----")
        await asyncio.sleep(150)

@bot.event
async def on_ready():
    channel = bot.get_channel(1197770600178003981)
    slinx_channel = bot.get_channel(1042064947867287646)
    randomnum = randint(1, 20)
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
    try:
        wakeup_splash = choice(wakeup_splashes)
        await channel.send(eval(f'f"{wakeup_splash}"'))
    except: print('somehow failed to send message?????')
    if randomnum == 1:
        try:
            wakeup_splash = choice(wakeup_splashes)
            await slinx_channel.send(eval(f'f"{wakeup_splash}"'))
        except: print('somehow failed to send message????')
    
    bot.loop.create_task(spamking_cycle())

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    msg = message.content
    msgl = msg.lower()
    channels=open("spamking channels.txt").read().split()
    global counterr
    # replies below
    if f"hello <@{bot.user.id}>" in msgl:
        await message.reply(choice([f"hello {message.author.name}" ]))
    if "bitboks batl s abotminom <:normal:1173301276851843122><:normal:1173301276851843122>" in msg and message.author.id != bot.user.id:
        if message.channel.id in channels:
            if counterr < 100:
                counterr+=1
                print(f"replying to abotmin with the same message part {counterr}")
                await message.reply("bitboks batl s abotminom <:normal:1173301276851843122><:normal:1173301276851843122>")
            else:
                await message.reply("битбокс баттл закончен")
                counterr = 0
        else:
            await message.channel.send("i will not spam outside spamking channels")
            await message.reply("битбокс баттл закончен")
            counterr = 0
    if msg == "yes i leaked your token 😃😃😃🫠🫠👼🖨️🕳️🔥🤗🤗😘😘":
        await message.reply("fuck what do i do now")
    if msg == "заткнись курица 🐔😂😂😂😔😔😔":
        await message.reply("сам ты курица и сам ты заткнись")
    # commands below
    if msg == "hey bartholomew list staring cat emojis":
        messaage = ''
        for guild in bot.guilds:
            messaage = f'{guild.name} stаring cаts: '
            a = False
            for emoji in guild.emojis:
                if 'staring_cat' in emoji.name:
                    a = True
                    animated = emoji.animated
                    messaage += "<"
                    if animated:
                        messaage += "a"
                    messaage += f":{emoji.name}:{emoji.id}>"
                if 'staring' in emoji.name and 'cat' in emoji.name:
                    a = True
                    animated = emoji.animated
                    messaage += '<'
                    if animated:
                        messaage += 'a'
                    messaage += f":{emoji.name}:{emoji.id}>"
            if not a:
                messaage += 'None'
            messaage +="\n"
            await message.channel.send(messaage)
    if msgl == "hey bartholomew kys":
        if message.author.id == rech2020:
            await message.channel.send(file=disnake.File("metal_pipe_falling_sound.mp3"))
            print("i am dead")
            await asyncio.sleep(1)
            exit()
        else:
            await message.channel.send("nuh uh" or "no u")
            print(f"{message.author.name} tried to kill me but failed due to perms issue")

@bot.event
async def on_guild_join(guild):
    print(f"i have been added to {guild.name}")
    status_resync()

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
        print(f"wait a second... is that\nis that fucking {member.name}")
        print("you know what screw it i am going to ban that person")
        print("attempting to ban that person...")
        try:
            await member.guild.ban(member.id, delete_message_days=0, reason='is in retards list')
        except:
            print("i failed to ban that person, time for plan B")
            try: role = barhtolomew_server.get_role(1195957915916447744)
            except: role = member.guild.get_role(1195957915916447744)
            print(f"attempting to add role {role.name} to {member.name}")
            try: await member.add_roles(role)
            except:
                print(f"i have failed to add role {role.name} to {member.name}")
                if member.guild.id == barhtolomew_server:
                    moderator_only = bot.get_channel(1195940341438746714)
                    await moderator_only.send(f"hello <@&1195946019351973888> help\n<@{member.id}> has got past both our defences\nwe're fucking doomed i think")
    elif member.guild.id == 1195939785928364132:
        print(f"as you know by now that person joined the barhtolomew server if i put the id right")
        if member.id not in trusteds:
            try: role = barhtolomew_server.get_role(1199173994654486738)
            except: role = member.guild.get_role(1199173994654486738)
            print(f"attempting to add role {role.name} to {member.name}")
            try: await member.add_roles(role)
            except: print(f'i failed to add role {role.name} to {member.name}')
    await status_resync()


@bot.user_command()
async def avatar(inter, user):
    embed = disnake.Embed(title=str(user))
    embed.set_image(url=user.display_avatar.url)
    await inter.response.send_message(embed=embed)


@bot.slash_command(name="help")
async def help(ctx):
    embed = disnake.Embed(title='help')
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

@bot.command(name='fetch_invites')
async def fetch_invites(ctx, guild_id):
    if ctx.author.id not in trusteds:
        ctx.send('you are not in trusteds <:typing:1195957954193653990>')
        return
    try: guild_id = int(guild_id)
    except: await ctx.send('not an id <:typing:1195957954193653990>')
    guild = bot.get_guild(guild_id)
    if guild is None:
        await ctx.send('guild not found.')
        return

    try:
        invites = await guild.invites()
        for invite in invites:
            await ctx.send(f'Invite url: {invite.url}, uses: {invite.uses}, inviter: {invite.inviter.name}, expiration date: {invite.expires_at}')
    except Exception as e:
        await ctx.send(f'An error occurred: {e}')

@bot.command()
async def get_perms(ctx, guild_id):
    if ctx.author.id not in trusteds:
        ctx.send('you are not in trusteds <:typing:1195957954193653990>')
        return
    try: guild_id = int(guild_id)
    except: await ctx.send('not an id <:typing:1195957954193653990>')
    guild = bot.get_guild(guild_id)
    member = guild.get_member(bot.user.id)
    perms = choice(guild.text_channels).permissions_for(member)
    message = 'Permissions:'
    for perm in perms:
        message += f'{perm}\n'
    await ctx.send(message)

@bot.slash_command(name='send_splashes_here', description='(OWNER ONLY) make bartholomew send splashes in here since start or reload')
async def send_splashes_here(ctx):
    if ctx.author.id==ctx.guild.owner_id or rech2020:
        file=open('spamking channels.txt').read().split()
        if str(ctx.channel.id) in file:
            remove_line("spamking channels.txt", str(ctx.channel.id))
            await ctx.send(f"i removed **#{ctx.channel}** from spamking channels")
        else:
            # credits to tema5002 for temalib
            add_line("spamking channels.txt", str(ctx.channel.id))
            await ctx.send(f"i added **#{ctx.channel}** to spamking channels")
    else:
        await ctx.send("You are not server owner", ephemeral=True)

@bot.slash_command(name='send_splash', description='send a splash')
async def send_splash(ctx, id:int):
    id-=1
    lensplashes=len(splashes)
    if 0<=id<lensplashes:
        embed=disnake.Embed(title=f"splash number {id+1} out of {lensplashes}",description=splashes[id])
    else:
        id=randint(0,lensplashes-1)
        embed=disnake.Embed(title=f"here is a random splash (№{id+1}/{lensplashes})",description=splashes[id])
    footer_dict={"text": splashes_descriptions[id]}
    embed.set_footer(**footer_dict)
    await ctx.send(embed=embed)

@bot.slash_command(name='send_wakeup_splash', description='send a wakeup splash')
async def send_wakeup_splash(ctx, id:int):
    id-=1
    lensplashes=len(wakeup_splashes)
    if 0<=id<lensplashes:
        embed=disnake.Embed(title=f"wakeup splash number {id+1} out of {lensplashes}",description=wakeup_splashes[id])
    else:
        id=randint(0,lensplashes-1)
        embed=disnake.Embed(title=f"here is a random splash (№{id+1}/{lensplashes})",description=wakeup_splashes[id])
    footer_dict={"text": wakeup_splashes_descriptions[id]}
    embed.set_footer(**footer_dict)
    await ctx.send(embed=embed)

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
        while len(message) < 2000-6:
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
    try: await ctx.send('```' + message + '```', ephemeral=True)
    except: await ctx.send('message got to long and it broke', ephemeral=True)

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
    try:
        await ctx.send(
            f"hello please make this work",
            components=[
                disnake.ui.Button(
                    label="word",
                    style=disnake.ButtonStyle.secondary,
                    custom_id="word2",
                ),
                disnake.ui.Button(
                    label="sentence",
                    style=disnake.ButtonStyle.secondary,
                    custom_id="sentence2",
                ),
                disnake.ui.Button(
                    label="text",
                    style=disnake.ButtonStyle.secondary,
                    custom_id="text2",
                ),
                ],
        )
    except:
        await ctx.send("it didn't work for some reason")

@bot.listen("on_button_click")
async def gibberish_listener(ctx: disnake.MessageInteraction):
    if ctx.component.custom_id not in ["word2", "sentence2", "text2"]:
        return

    if ctx.component.custom_id == "word2":
        await ctx.send(f"here's your gibberish word: {gib.generate_word()}")
    elif ctx.component.custom_id == "sentence2":
        await ctx.send(f"here's your gibberish sentence: {gen_sentence2()}")
    elif ctx.component.custom_id == "text2":
        await ctx.send(f"here's a gibberish text:\n```\n{gen_text2()}\n```")

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
async def glibberish_listener(ctx: disnake.MessageInteraction):
    if ctx.component.custom_id not in ["word", "sentence", "text"]:
        return

    if ctx.component.custom_id == "word":
        await ctx.send(f"here's your glibberish word: {gen_word()}")
    elif ctx.component.custom_id == "sentence":
        await ctx.send(f"here's your glibberish sentence: {gen_sentence()}")
    elif ctx.component.custom_id == "text":
        await ctx.send(f"here's a glibberish text:\n```\n{gen_text()}\n```")

@bot.slash_command(name="save_file", description="i swear i didn't steal this command from ammeter (lying)")
async def save_file(ctx, file: disnake.Attachment, filename: str = disnake.Attachment.filename):
    await ctx.response.defer()
    if not ctx.author.id in save_file_trusteds:
        await ctx.send("you must be in trusted list to use this command",ephemeral=True)
    elif file.size > 5*1024*1024:
        await ctx.send(f"this file weights more than **5** MB! (~**{math.ceil(file.size/1024)}** KB)")
    else:
        now = datetime.datetime.now()
        last_used = save_file_cooldowns.get(ctx.author.id)
        if last_used is not None:
            when_used = (now - last_used).total_seconds()
            if when_used < 60:
                await ctx.send(f"this command is on cooldown <:typing:1133071627370897580>\ntry again in {round(60 - when_used)} seconds", ephemeral=True)
                return
        save_file_cooldowns[ctx.author.id] = now
        if "." in file.filename:
            filepath = get_file_path(__file__, "shitpost", filename+file.filename[file.filename.rfind("."):])
        else:
            filepath = get_file_path(__file__, "shitpost", filename)
        try:
            await file.save(filepath)
            await ctx.send(f"File saved successfully as '{filepath}'.")
            channel=bot.get_channel(1197770600178003981)
            await channel.send(f"**{ctx.author.name}** aka user with id `{ctx.author.id}` added file {filename}")
        except Exception as e:
            await ctx.send(f"An error occurred while saving the file: {e}")


@bot.slash_command(name="list_files", description="lists all files saved with /save_file")
async def list_files(ctx):
    embed=makeembed(1, os.listdir("shitpost"))
    await ctx.send(embed=embed, components=makecomponents(embed.title))

@bot.slash_command(name="send_file", description="sends any file saved using with /save_file")
async def send_file(ctx, filename: str):
    await ctx.response.defer()
    if not filename in os.listdir("shitpost"):
        await ctx.send(f"file `{filename}` doesnt exist", ephemeral=True)
    else:
        now = datetime.datetime.now()
        last_used = send_file_cooldowns.get(ctx.author.id)

        if last_used is not None:
            # time since last use
            when_used = (now - last_used).total_seconds()

            if when_used < 20:
                await ctx.send(f"this command is on cooldown <:typing:1133071627370897580>\ntry again in {round(20 - when_used)} seconds", ephemeral=True)
                return

        send_file_cooldowns[ctx.author.id] = now
        await ctx.send(filename, file=disnake.File(get_file_path(__file__, "shitpost", filename)))


@bot.slash_command(name="sort", description="Sort file")
async def send_file(ctx, file: disnake.Attachment):
    await ctx.response.defer()
    if file.size > 128*1024:
        await ctx.send(f"this file weights more than **128** KB! (~**{math.ceil(file.size/1024)}** KB)")
    elif file.filename[file.filename.rfind(".")+1:] != "txt":
        h=file.filename[file.filename.rfind(".")+1:]
        await ctx.send(f"this is not a txt file :skull: ({h})")
    else:
        await file.save(get_file_path(__file__, "temp", "input.txt"))
        with open(get_file_path(__file__, "temp", "output.txt"),"w") as output:
            for every in sorted(open(get_file_path(__file__,"temp", "input.txt")).readlines()): output.write(every)
        await ctx.send(file.filename, file=disnake.File(get_file_path(__file__, "temp", "output.txt")))

@bot.slash_command(name='кгыышфт_to_english_translator', description='translate russian gibberish to english')
async def translator1(ctx, text: str):
    replaces=[('й','q'),('ц','w'),('у','e'),('к','r'),('е','t'),('н','y'),('г','u'),('ш','i'),('щ','o'),('з','p'),('х','['),('ъ',']'),('ф','a'),('ы','s'),('в','d'),('а','f'),('п','g'),('р','h'),('о','j'),('л','k'),('д','l'),('ж',';'),('э',"'"),('я','z'),('ч','x'),('с','c'),('м','v'),('и','b'),('т','n'),('ь','m'),('б',','),('ю','.'),('ё','`')]
    replaces_upper=[(a.upper(),b.upper()) for (a,b) in replaces]
    for a, b in replaces:
        text = text.replace(a,b)
    for a, b in replaces_upper:
        text = text.replace(a,b)
    await ctx.send(text)

@bot.slash_command(name='english_to_кгыышфт_translator', description='translate english to russian gibberish')
async def translator2(ctx, text: str):
    replaces=[('й','q'),('ц','w'),('у','e'),('к','r'),('е','t'),('н','y'),('г','u'),('ш','i'),('щ','o'),('з','p'),('х','['),('ъ',']'),('ф','a'),('ы','s'),('в','d'),('а','f'),('п','g'),('р','h'),('о','j'),('л','k'),('д','l'),('ж',';'),('э',"'"),('я','z'),('ч','x'),('с','c'),('м','v'),('и','b'),('т','n'),('ь','m'),('б',','),('ю','.'),('ё','`')]
    replaces_upper=[(a.upper(),b.upper()) for (a,b) in replaces]
    for a, b in replaces:
        text = text.replace(b,a)
    for a, b in replaces_upper:
        text = text.replace(b,a)
    await ctx.send(text)

@bot.slash_command(name='kick', description='kick people')
async def kick(ctx, member: disnake.Member, *, reason='skill issue'):
    if ctx.author.id != rech2020:
        await ctx.send("perms issue", ephemeral=True)
        return
    permissions = ctx.guild.me.guild_permissions
    if permissions.kick_members:
        await member.send(f"hey loser you got kicked from {ctx.guild.name} for `{reason}`")
        await member.kick(reason=reason)
        await ctx.send(f"kicked member {member.name} from {ctx.guild.name} for {reason}",ephemeral=True)
        await log_channel.send(f"kicked member {member.name} from {ctx.guild.name} for {reason}",ephemeral=True)
    else:
        await ctx.send("i don't have permissions", ephemeral=True)

@bot.command(name="die")
async def die(ctx):
    if ctx.author.id in trusteds:
        await ctx.send(file=disnake.File("metal_pipe_falling_sound.mp3"))
        print("i am dead")
        await asyncio.sleep(1)
        exit()
    else:
        await ctx.send("nuh uh")
        print(f"{ctx.author.name} tried to kill me but failed due to perms issue")

@bot.command(name='reload')
async def reload(ctx):
    await ctx.send('ok wait')
    subprocess.Popen(['python', 'main.py'])
    sys.exit(0)

@bot.command(name='shutdown')
async def shutdown(ctx):
    if ctx.author.id == rech2020:
        await ctx.send('shutting down...')
        os.system('shutdown /s')
    elif ctx.author.id in trusteds:
        await ctx.send('shutting down... (totally)')
        print(f"{ctx.author.name} tried to shut me down and i pretended that i got shut down")
        return
    else:
        await ctx.send("perms issue")
        try: await log_channel.send(f"{ctx.author.name} tried to shutdown the device i am being hosted on")
        except:
            channel = bot.get_channel(1197770600178003981)
            await channel.send(f"{ctx.author.name} tried to shutdown the device i am being hosted on")
        print(f"{ctx.author.name} tried to shutdown the device i am being hosted on")

bot.load_extension("cogs.ping")

bot.run(open("token.txt").read())
