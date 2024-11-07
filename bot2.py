import discord
from discord.ext import commands
import random
from bot_mantik import gen_pass, yazi_tura, kalp  

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command(name='kalp')
async def kalp(ctx):
    sonuc = kalp()  
    await ctx.send(sonuc)

@bot.command(name='yazi_tura')
async def yazi_tura(ctx):
    sonuc = yazi_tura() 
    await ctx.send(sonuc)
    
@bot.command(name='parola')
async def parola(ctx):
    sonuc = gen_pass(pass_length=10) 
    await ctx.send(sonuc)

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)







bot.run("")