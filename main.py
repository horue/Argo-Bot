import discord
from discord.ext import commands
import os
import json
import random
import datetime
from key import key
from lists.images import *
from modules.info import *
from modules.rolls import *
from modules.generators import *
from modules.interactions import *
from modules.images import *
from modules.phrases import *
from modules.miscellaneous import *
from modules.error_handler import *

from assets.colors import *
from assets.support_functions import *

#from embeds.help import *




async def load_prefix(bot, message):
    server = str(message.guild.id)
    try:
        with open(r'common_data\prefixes.json', 'r', encoding='utf-8') as p:
            prefixes = json.load(p)
        final_prefix = prefixes.get(server, {}).get('prefix', '-')
    except FileNotFoundError:
        final_prefix = '-'
    return final_prefix



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(
   command_prefix = load_prefix,
   case_insensitive = True,
   activity=discord.CustomActivity(name="Para ajuda use '-ajuda'"),
   status=discord.Status.online,
   intents=intents)
versao = ('0.1.0')



## Bancos de dado ##

cara_coroa = ["Cara", "Coroa"]

## Básicos ##

@bot.event
async def on_ready():
  formated_print('INFO', 'Success:', 'logged in with ')
  print('{0.user}' . format(bot))

## Informações ##


@bot.command()
async def log(ctx):
  await Info.log(ctx)


@bot.command(aliases=['versão', 'versao', 'ver'])
async def version(ctx):
  await Info.version(ctx)


@bot.command(aliases=['bom dia', 'boa tarde', 'boa noite'])
async def olá(ctx):
  await ctx.send(f'Sempre é hora de dar um bom dia. Então, bom dia, {ctx.author.mention}!')

@bot.command()
async def frase(ctx):
  await Quote.qotd(ctx)


@bot.command()
async def servidor(ctx):
  await Info.servidor(ctx)


@bot.command()
async def sugestão(ctx):
  await Info.sugestao(ctx)


@bot.command()
async def l(ctx):
  await Info.l(ctx)


## Rolls ##


@bot.command(aliases=['r', 'dado', 'dice'])
async def roll(ctx, info, conta='', ficha=''):
  await Dice.roll(ctx, info, conta, ficha)



@bot.command()
async def moeda(ctx):
  await Coin.moeda(ctx)


@bot.command(aliases=['quantia', 'a'])
async def amount(ctx,min=100,max=500):
  amount = random.randint(min,max)
  await ctx.send(f'{ctx.author.mention} 🎇 \n**Como resultado desse duelo, você ganhou**: {amount}')


## Character Generation ##


@bot.command()
async def per(ctx):
  await CharacterCreator.modernCharacter(ctx)


@bot.command(aliases=['personagem medieval'])
async def permedi(ctx):
  await CharacterCreator.medievalCharacter(ctx)

@bot.command()
async def maha(ctx):
  await Quote.maha(ctx)


## Member Interactions ##


@bot.command()
async def hug(ctx, member: discord.Member):
  user = member
  await Interact.hug(ctx, user)

@bot.command()
async def kiss(ctx, user: discord.Member):
  await Interact.kiss(ctx, user)


@bot.command()
async def eat(ctx, user: discord.Member):
  await Interact.nani(ctx, user)


## Custom Prefix ##

@bot.command()
async def prefix(ctx, prefix):
    try:
        if prefix == '':
          final_prefix = load_prefix(bot, message=prefix)
          await ctx.send(f'O prefixo do servidor é: {final_prefix}')
        else:
          with open(r'common_data\prefixes.json', 'r', encoding='utf-8') as p:
              prefixes = json.load(p)
    except FileNotFoundError:
        prefixes = {}
    server_id = str(ctx.message.guild.id)
    prefixes[server_id] = {"prefix": prefix}
    with open(r'common_data\prefixes.json', 'w', encoding='utf-8') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'O prefixo do servidor foi alterado para {prefix}.')


## Utilidades ##


@bot.command(aliases=['foto', 'imagem'])
async def avatar(ctx, member: discord.Member):
  show_avatar = discord.Embed(
    title = f'Aqui está a foto dele, senhor {ctx.author}',
    color = 2602879
  )
  show_avatar.set_image(url='{}'.format(member.display_avatar.url))
  await ctx.send(f'{ctx.author.mention}', embed=show_avatar)


## Memes ##

   

@bot.command(aliases=['sessão?'])
async def sessão(ctx):
  await Misc.sessão(ctx)


@bot.command(aliases=['rec', 'sug', 'sugerir'])
async def recomendar(ctx):
  await Misc.recomendar(ctx)


@bot.command()
async def pobre(ctx):
  await Misc.pobre(ctx)


@bot.command()
async def multi(ctx):
  await Misc.multi(ctx)

## Images ##


@bot.command(aliases=['waifu', 'wa', 'garota', 'girl'])
async def anime(ctx, category):
  await AnimeImage.waifu(ctx, category)


@bot.command()
async def trap(ctx):
  await AnimeImage.trap(ctx)



@bot.command()
async def art(ctx):
  try:
    print(1)
  except:
    print('a')




## Música ##

@bot.command()
async def joi(ctx):
  canal = ctx.author.voice.voice_channel
  await bot.join_voice_channel(canal)


@bot.command()
async def join(ctx):
    if not ctx.message.author.voice_channel:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


## Embeds ##


#@bot.command()
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
    await ErrorHandler.on_command_error(ctx, error)


def run_bot():
  os.system('cls')
  bot.run(key)


if __name__ == "__main__":
  run_bot()