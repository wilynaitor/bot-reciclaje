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
async def ayuda(ctx):
    help_text = (
        "**♻️ BOT DE RECICLAJE ♻️**\n\n"
        "**!amarillo** → Envases de plástico\n"
        "**!azul** → Papel y cartón\n"
        "**!verde** → Vidrio\n"
        "**!marron** → Residuos orgánicos\n"
        "**!gris** → Basura general\n"
        "**!mem** → Envía una imagen aleatoria\n"
        "**!trivia** → Pregunta de trivia sobre reciclaje\n"
        "**!tip** → Consejo ecológico\n"
    )
    await ctx.send(help_text)

@bot.command()
async def amarillo(ctx):
    embed = discord.Embed(
        title="🟡 Contenedor Amarillo",
        description="Aquí van **envases de plástico**, **latas** y **briks**.",
        color=discord.Color.yellow()
    )
    await ctx.send(embed=embed)


@bot.command()
async def azul(ctx):
    embed = discord.Embed(
        title="🔵 Contenedor Azul",
        description="Aquí van **papel** y **cartón**.",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def verde(ctx):
    embed = discord.Embed(
        title="🟢 Contenedor Verde",
        description="Aquí va **vidrio**.",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

@bot.command()
async def marron(ctx):
    embed = discord.Embed(
        title="🟤 Contenedor Marrón",
        description="Aquí van **residuos orgánicos**.",
        color=discord.Color.dark_gold()
    )
    await ctx.send(embed=embed)

@bot.command()
async def gris(ctx):
    embed = discord.Embed(
        title="⚫ Contenedor Gris",
        description="Aquí va **basura general**.",
        color=discord.Color.dark_grey()
    )
    await ctx.send(embed=embed)

preguntas = [
    ("¿En qué contenedor va una botella de vidrio?", "verde"),
    ("¿Dónde tiras una caja de pizza con grasa?", "gris"),
    ("¿Qué contenedor es para el cartón?", "azul")
]

@bot.command()
async def trivia(ctx):
    pregunta, respuesta = random.choice(preguntas)
    await ctx.send(pregunta)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    msg = await bot.wait_for("message", check=check)
    if msg.content.lower() == respuesta:
        await ctx.send("✅ ¡Correcto!")
    else:
        await ctx.send(f"❌ No, la respuesta era **{respuesta}**.")

tips = [
    "🌱 Usa botellas reutilizables.",
    "🚴‍♂️ Evita el coche para trayectos cortos.",
    "🛒 Compra productos locales."
]

@bot.command()
async def tip(ctx):
    await ctx.send(random.choice(tips))


@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run("Token")

