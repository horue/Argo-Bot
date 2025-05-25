import discord
from discord.ext import commands
import os
import requests
import json
import random
import datetime
from key import key
from lists import *
from modules.info import *
from modules.rolls import *
from modules.generators import *
from modules.interactions import *

from assets.colors import *

#from embeds.help import *


os.chdir("D:\\Users\\Eu\\Desktop\\(Audiovisual)\\Argo-Bot")


async def load_prefix(bot, message):
    server = str(message.guild.id)
    try:
        with open('sample.json', 'r', encoding='utf-8') as p:
            prefixes = json.load(p)
        final_prefix = prefixes.get(server, {}).get('prefix', '-')
    except FileNotFoundError:
        final_prefix = '-'
    return final_prefix



intents = discord.Intents.default()
intents.message_content = True
bot = client = commands.Bot(
   command_prefix = load_prefix,
   case_insensitive = True,
   activity=discord.CustomActivity(name="Para ajuda use '-ajuda'"),
   status=discord.Status.online,
   intents=intents)
versao = ('0.1.0')



## Bancos de dado ##

cara_coroa = ["Cara", "Coroa"]

## Básicos ##


@client.event
async def on_ready():
  now = datetime.datetime.now()
  formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
  print(f'{GREY}{formatted_datetime}{RESET} {BLUE}{'INFO'}{RESET}     {GREEN}Success: {RESET}' + 'logged in with '+'{0.user}' . format(bot))

## Informações ##


@client.command()
async def log(ctx):
  await Info.log(ctx)


@client.command(aliases=['versão', 'versao', 'ver'])
async def version(ctx):
  await Info.version(ctx)


@client.command(aliases=['bom dia', 'boa tarde', 'boa noite'])
async def olá(ctx):
  await ctx.send(f'Sempre é hora de dar um bom dia. Então, bom dia, {ctx.author.mention}!')

@client.command()
async def frase(ctx):
  await ctx.send(random.choice(frases_do_dia))


@client.command()
async def servidor(ctx):
  await Info.servidor(ctx)


@client.command()
async def l(ctx):
  await Info.l(ctx)


## Rolls ##


@client.command(aliases=['r', 'dado', 'dice'])
async def roll(ctx, info, conta='', ficha=''):
  await Dice.roll(ctx, info, conta, ficha)



@client.command()
async def moeda(ctx):
  await Coin.moeda(ctx)


@client.command(aliases=['quantia', 'a'])
async def amount(ctx,min=100,max=500):
  amount = random.randint(min,max)
  await ctx.send(f'{ctx.author.mention} 🎇 \n**Como resultado desse duelo, você ganhou**: {amount}')


## Character Generation ##


@client.command()
async def per(ctx):
  await CharacterCreator.modernCharacter(ctx)


@client.command(aliases=['personagem medieval'])
async def permedi(ctx):
  await CharacterCreator.medievalCharacter(ctx)

@client.command()
async def maha(ctx):
  await ctx.send(random.choice(mahaa))


## Member Interactions ##


@client.command()
async def hug(ctx, user: discord.Member):
  await Interaction.hug(ctx, user)

@client.command()
async def kiss(ctx, user: discord.Member):
  await Interaction.kiss(ctx, user)


@client.command()
async def eat(ctx, user: discord.Member):
  await Interaction.nani(ctx, user)

@client.command()
async def jav(ctx):
  japae = discord.Embed(
    title = f'As coisas estão ficando quentes por aqui!',
    description = f'{ctx.author.mention} eu não acredito que você está vendo esse tipo de coisa!',
    color = 2602879
  )

  japae.set_image(url=(random.choice(japa)))
  
  await ctx.send(f'**{ctx.author.mention}**')
  await ctx.send(embed = japae)


## Custom Prefix ##

@client.command()
async def prefix(ctx, prefix):
    try:
        if prefix == '':
          final_prefix = load_prefix(bot, message=prefix)
          await ctx.send(f'O prefixo do servidor é: {final_prefix}')
        else:
          with open('sample.json', 'r', encoding='utf-8') as p:
              prefixes = json.load(p)
    except FileNotFoundError:
        prefixes = {}
    server_id = str(ctx.message.guild.id)
    prefixes[server_id] = {"prefix": prefix}
    with open('sample.json', 'w', encoding='utf-8') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'O prefixo do servidor foi alterado para {prefix}.')


## Utilidades ##


@client.command(aliases=['foto', 'imagem'])
async def avatar(ctx, member: discord.Member):
  show_avatar = discord.Embed(
    title = f'Aqui está a foto dele, senhor {ctx.author}',
    color = 2602879
  )
  show_avatar.set_image(url='{}'.format(member.display_avatar.url))
  await ctx.send(f'{ctx.author.mention}', embed=show_avatar)


@client.command()
async def sugestão(ctx):
  await ctx.send(f'{ctx.author.mention}, você pode enviar uma sugestão de comando por este link: https://bit.ly/3uwBLfb')


## Memes ##

   

@client.command(aliases=['sessão?'])
async def sessão(ctx):
  await ctx.send('Eu ouvi sessão?')


@client.command(aliases=['rec', 'sug', 'sugerir'])
async def recomendar(ctx):
  await ctx.send(f'**{ctx.author.mention}, minha recomendação pra você é**: {random.choice(suguestão)}')


@client.command()
async def trap(ctx):
  await ctx.send(random.choice(traps))



@client.command()
async def pobre(ctx):
  await ctx.send ('https://imgur.com/S8uJQVm')


@client.command()
async def multi(ctx):
  await ctx.send('esse jogo e multi, voces nao tem idea da mídia do ps4 eles pagam pelo jogo que voces jogam sao mais caros e mais evoluídos assim e diferente e voce nunca ira entender pois sao infieis ao console')


## Images ##


@client.command(aliases=['waifu', 'wa', 'garota', 'girl'])
async def anime(ctx, category = 'waifu'):
  try:
      r = requests.get(f'https://api.waifu.pics/sfw/{category}')
      data = r.json()
      url = data['url']
      await ctx.send(url)
  except:
     await ctx.send(f'Erro.')


@client.command()
async def art(ctx):
  try:
    print(1)
  except:
    print('a')




## Música ##

@client.command()
async def joi(ctx):
  canal = ctx.author.voice.voice_channel
  await client.join_voice_channel(canal)


@client.command()
async def join(ctx):
    if not ctx.message.author.voice_channel:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


## Embeds ##


#@client.command()
#async def ajudaa(ctx):
#  await ctx.send(embed = ajuda)


## Erros ##



@avatar.error
async def avatar_handler(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send(f'Alô? Esqueceu de marcar de quem você quer a foto, {ctx.author.mention}!')


@anime.error
async def avatar_handler(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send(f'Tá na Disney, meu querido? Esse comando não existe!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(random.choice(error_message))


client.run(key)