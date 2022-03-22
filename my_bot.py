#Import Discord Package
import discord
import random
import requests
import json
from discord.ext import commands

# CONECTANDO COM API, TMJ AXEL

response = requests.get("https://api.opendota.com/api/heroes")
heroesResponse = response.json()

herois = []

for n in heroesResponse:

    name = n['localized_name']
    herois.append(name)

print(herois)

response2 = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao = response2.json()

cotacao_euro=cotacao['EURBRL']['bid']
cotacao_dolar=cotacao['USDBRL']['bid']
cotacao_bitcoin=cotacao['BTCBRL']['bid']


#Client(our bot) as coisas q o bot faz
client = commands.Bot(command_prefix='--')

@client.command(name='sortear')
async def sortear(context):
    elemento = random.choice(herois)
    await context.message.channel.send('hero escolhido foi ' + elemento)

@client.command(name='Shuiten')
async def Shuiten(context):
    await context.message.channel.send('O cara é BRABO')

@client.command(name='Axel')
async def Shuiten(context):
    await context.message.channel.send('Burro')

@client.command(name='Vit')
async def Shuiten(context):
    await context.message.channel.send('Noob')

@client.command(name='Joba')
async def Shuiten(context):
    await context.message.channel.send('Gay')

@client.command(name='Sempra')
async def Shuiten(context):
    await context.message.channel.send('Da o cu')

@client.command(name='bitcoin')
async def Shuiten(context):
    await context.message.channel.send('O bitcoin nesse momento ta R$'+cotacao_bitcoin+' dureza bro')

@client.command(name='dolar')
async def Shuiten(context):
    await context.message.channel.send('O dolar nesse momento ta R$'+cotacao_dolar+' caro p krl kkkk')

@client.command(name='euro')
async def Shuiten(context):
    await context.message.channel.send('O euro nesse momento ta R$'+cotacao_euro+' ossada ne man') 

@client.event
async def on_ready():
    #DO STUFF

    general_channel = client.get_channel(384411956465106948)
    await general_channel.send('Salve, rapeiz. Rick na área...')

@client.event
async def on_message(message):
    if message.content == 'quem eh o melhor jogador de dota do mundo?':
        general_channel = client.get_channel(384411956465106948)
        await general_channel.send('Shuiten, sem dúvidas')
    await client.process_commands(message)

#rodar o cliente no server do disc
client.run('OTMyNjI4OTg4NjkyNjcyNTUy.YeVwbg.vbtgLI2oPRo8SiDwgJIQexNdauU')