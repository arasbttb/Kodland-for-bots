import discord
import random
from bot_mantik import gen_pass
from bot_mantik import yazi_tura
from bot_mantik import kalp


intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
        
    if message.content.startswith('$sifre'):
        await message.channel.send(gen_pass(pass_length=10))
        
    if message.content.startswith('$yazı_tura'):
        await message.channel.send(yazi_tura())
        
    if message.content.startswith('$kalp'):
        await message.channel.send(kalp())
        
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(gen_pass(pass_length=10))

client.run("")
