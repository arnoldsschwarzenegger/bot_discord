import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?',  intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')


@bot.command()
async def mem_programowanie(ctx):
    lista = os.listdir('programowanie')
    img_name = random.choice(lista)
    with open(f'programowanie/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem_zwierzeta(ctx):
    lista2 = os.listdir('zwierzeta')
    img_name = random.choice(lista2)
    with open(f'zwierzeta/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("TOKEN")
