import discord
import random
from discord.ext import commands
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def amarillo(ctx):
    await ctx.send('¡En ese contenedor van envases de plastico!')

@bot.command()
async def azul(ctx):
    await ctx.send('¡En ese contenedor van el papel y el carton!')

@bot.command()
async def verde(ctx):
    await ctx.send('¡Para vidrio limpio y fresco bro!')

@bot.command()
async def marron(ctx):
    await ctx.send('¡Para residuos organicos como cascaras de frutas!')

@bot.command()
async def gris(ctx):
    await ctx.send('¡Basura, solo eso!')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run("Token")
