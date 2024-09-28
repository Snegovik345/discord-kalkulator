import discord
import math
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

commandss = ["Сложение", "Вычитание", "Деление", "Умножение", "Высчитывание корня"]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def sum(ctx, a, b):
    await ctx.send(int(a) + int(b))

@bot.command()
async def mines(ctx, a, b):
    await ctx.send(int(a) - int(b))

@bot.command()
async def multiply(ctx, a, b):
    await ctx.send(int(a) * int(b))

@bot.command()
async def division(ctx, a, b):
    if int(b) == 0:
        await ctx.send("Ошибка: Деление на ноль")
    else:
        await ctx.send(int(a) / int(b))

@bot.command()
async def degree(ctx, a, b):
    await ctx.send(int(a) ** int(b))

@bot.command()
async def koren(ctx, a):
    await ctx.send(math.sqrt(int(a)))

@bot.command()
async def comlist(ctx):
    await ctx.send("Привет! Вот что я умею:\n" + "\n".join(commandss))


bot.run
