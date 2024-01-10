import disnake
from disnake.ext import commands

bot = commands.Bot(reload=True)

@bot.event
async def on_ready():
    print("Powerup inniciated.")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")

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
        # We filter out any other button presses except
        # the components we wish to process.
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

@bot.slash_command(name='user_info', description='get some info about your account')
async def user_info(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message(f"Your tag: {inter.author}\nYour ID: {inter.author.id}")

bot.load_extension("cogs.ping")

bot.run(open("token.txt").read())