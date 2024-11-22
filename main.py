import discord
import random
import os
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("photos"))
    with open(f'photos/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def animals(ctx):
    img_name = random.choice(os.listdir("animals"))
    with open(f'animals/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("")
