import discord # Подключаем библиотеку
from discord.ext import commands

intents = discord.Intents.default() 
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents) 

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run('MTE4MTc4OTM3MzU0MTM5MjM4NA.GFznNM.BAF-b3Qbw5GQgVugCxcYOYey98XPTBx8PcQNMc')