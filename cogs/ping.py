import disnake
from disnake.ext import commands


class PingCommand(commands.Cog):
    """this will be a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="get bot's brain delay or something",)
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """get how long it takes for bot to respond or something."""
        await inter.response.send_message(f"uuuh pong\n rech2020 or whoever is hosting the bot is melting the device with the bot that has brain delay of {round(self.bot.latency * 1000)}ms")


def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))