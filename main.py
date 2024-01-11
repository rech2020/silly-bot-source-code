import disnake
from disnake.ext import commands

bot = commands.Bot(reload=True)

@bot.event
async def on_ready():
    print("Powerup inniciated.")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")
    
    print("setting presence")
    people=0
    for every in bot.guilds:
        people+=every.member_count
        print(f"{people} people... ({every.member_count} people from {every.name})")
    await bot.change_presence(status=disnake.Status.online,activity=disnake.Game(f"with {people} people on {len(bot.guilds)} servers"))
    print("presence changed")

@bot.user_command()
async def avatar(inter, user):
    embed = disnake.Embed(title=str(user))
    embed.set_image(url=user.display_avatar.url)
    await inter.response.send_message(embed=embed)

@bot.slash_command(name='buttons', description='testing buttons')
async def buttons(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(
        "test",
        components=[
            disnake.ui.Button(label="testing testing 1 2 3", style=disnake.ButtonStyle.success, custom_id="success"),
            disnake.ui.Button(label="danger button", style=disnake.ButtonStyle.danger, custom_id="danger"),
        ],
    )


@bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["success", "danger"]:
        return

    if inter.component.custom_id == "success":
        await inter.response.send_message("test success")
    elif inter.component.custom_id == "danger":
        await inter.response.send_message("do not press the danger button")

@bot.slash_command(name='server_info', description='get server info or something')
async def server_info(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(
        f"Server name: {inter.guild.name}\nTotal members: {inter.guild.member_count}"
    )

@bot.slash_command(name="say",description="talk as a bot")
async def say(ctx, text:str, guild_id:str = None, channel_id: str = None):
  if guild_id is None:
      guild_id = ctx.guild.id
  else:
    try:
      guild_id = int(guild_id)
    except:
      await ctx.send("invalid guild id",ephemeral=True)
      return
  if channel_id is None:
      channel_id = ctx.channel.id
  else:
    try:
      channel_id = int(channel_id)
    except:
      await ctx.send("invalid channel id",ephemeral=True)
      return
  if ctx.author.id==710621353128099901 or ctx.author.id==ctx.guild.owner_id:
      await ctx.send("ok", ephemeral=True)
      guild = bot.get_guild(guild_id)
      channel = guild.get_channel(channel_id)
      await channel.send(text)
      print(f"{ctx.author.name} used /say to say in {guild.name} #{channel.name}\n{text}")
  else:
      await ctx.send("nuh uh",ephemeral=True)

@bot.slash_command(name='guild_info', description='get info about a guild aka server')
async def guild_info(inter, guild_id: int=938770488702951545):
   guild = bot.get_guild(guild_id)
   if guild is None:
       await inter.response.send_message("Guild not found.")
       return

   message = f"Guild Name: {guild.name}\n"
   message += f"Guild ID: {guild.id}\n"
   message += f"Owner: {guild.owner}\n"
   message += f"Owner ID: {guild.owner_id}\n"
   message += f"Text channels: {len(guild.text_channels)}\n"
   message += f"Member Count: {guild.member_count}\n"
   print(message)
   await inter.response.send_message(message)
   print(f"Text channels but list:\n{guild.text_channels}\n")



@bot.slash_command(name='user_info', description='get some info about your account')
async def user_info(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(f"Your tag: {inter.author}\nYour ID: {inter.author.id}")

@bot.slash_command()
async def msg_console(ctx, msg):
    print(f'um hello {ctx.author.name} left a message fo you: {msg}')
    await ctx.send('done',ephemeral=True)
bot.load_extension("cogs.ping")

bot.run(open("token.txt").read())