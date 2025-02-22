import discord
import random
from discord.ext import commands
from model import classify

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh):
    await ctx.send("he" * count_heh)

@bot.command()
async def predict(ctx):
  try:
    if ctx.message.attachments:
      for attachment in ctx.message.attachments:
        file_name = attachment.filename
        await attachment.save(f'./img/{file_name}')

        await ctx.send(classify(f'./img/{file_name}'))
    else:
      await ctx.send("No image found")
  except:
    await ctx.send("Something went wrong :(")

@bot.command()
async def secim(ctx, *args):
  x = []
  for part in args:
    x.append(part)
  
  await ctx.send(random.choice(x))

bot.run("TOKEN")
