import discord
from discord.ext import commands
import os
import requests
import json
import random
from key import key
from lists import *
from embeds import *



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
bot = client = commands.Bot(command_prefix = load_prefix, case_insensitive = True, activity=discord.Game(name="Para ajuda use '-ajuda'"), status=discord.Status.online, intents=intents)
versao = ('0.0.2')


## Bancos de dado ##

cara_coroa = ["Cara", "Coroa"]

## Básicos ##


@client.event
async def on_ready():
  print('Entramos como {0.user}' . format(client))

@client.event
async def on_member_join(member):
  channel = discord.util.get(member.guild.channel, name='welcome')
  await channel.send(f'Bem vindo, {member.mention}! Lembre-se de tratar todos bem e de se divertir.')


## Informações ##


@client.command()
async def log(ctx):
  await ctx.send('Agora estou imparável!\nAntes de ir pras novidades, vamos as coisas que foram consertadas"\nAgora quando uma operação, usando os dados, daria um número negativo, ele vira 1! Até porque é impossível um dado negativo.\nForam adicionadas MUITAS novas imagens ao comando "anime", além disso também da pra ativar ele usando o "-wa".\nOutra coisa muito importante é que o "-avatar" foi muito implementado"! Agora quando tiver algo faltando ou algo de errado eu vou te avisar.\nAgora a única novidade dessa versão é que eu posso sugerir animes agora! Isso mesmo. Usando o comando "-sugerir" vou te sugerir um anime, acompanhado da página dele no MAL.\nPor fim, existem duas funções que estão sendo desenvolvidas. Por serem meio complexas, é capaz que ainda demore um pouco até eu ser capaz de fazê-las.\nEntão é isso, até a próxima versão!')


@client.command(aliases=['bom dia', 'boa tarde', 'boa noite'])
async def olá(ctx):
  await ctx.send(f'Sempre é hora de dar um bom dia. Então, bom dia, {ctx.author.mention}!')

@client.command()
async def frase(ctx):
  await ctx.send(random.choice(frases_do_dia))


@client.command()
async def servidor(ctx):
  await ctx.send(f'Sinta-se livre para entrar no meu servidor oficial, {ctx.author.mention}!\nAqui está o link: https://discord.gg/t2HBP7q37s')

@client.command()
async def l(ctx):
  await ctx.send("I lived, Bithces.")


## Rolls ##


@client.command(aliases=['r', 'dado', 'dice'])
async def roll(ctx, numero=20, conta='', ficha=''):
  rolagem = random.randint(1,int(numero))
  if conta == '':
        total = (int(rolagem))
  elif conta == '+':
         total = (int(rolagem) + int(ficha))
  elif conta == '-':
         total = (int(rolagem) - int(ficha))
  elif conta == 'x':
         total = (int(rolagem) * int(ficha))
  elif conta == '/':
         total = (int(rolagem) / int(ficha))
  if ficha == '':
          ficha = ''
  if total < 1:
          total = '1'
  if rolagem == 20:
          rolagem = '**20**'
  if rolagem == 1:
          rolagem = '**1**'
  await ctx.send(f'{ctx.author.mention} 🎇 \n**Resultado**: D{numero} ({rolagem}) {conta} {ficha}\n**Total**: {total}')


@client.command(aliases=['m', 'mr'])
async def multiroll(ctx, quantidade=1, numero=20):
  resultados=[]
  for i in range (quantidade):
    rolagem=random.randint(1,int(numero))
    resultados.append(rolagem)
  await ctx.send(f'{ctx.author.mention} 🎇 \n**Rolagem de**: {quantidade}d{numero}\n**Resultados**: {resultados}')



@client.command()
async def moeda(ctx):
  await ctx.send('E o resultado é...')
  await ctx.send('...')
  await ctx.send(random.choice(cara_coroa))



@client.command(aliases=['quantia', 'a'])
async def amount(ctx,min=500,max=500):
  dproll = random.randint(min,max)
  await ctx.send(f'{ctx.author.mention} 🎇 \n**Como resultado desse duelo, você ganhou**: {dproll}')


@client.command()
async def per(ctx):
  idade = random.randint(14,60)
  jobb = random.choice(menos25) if idade <= 25 else random.choice(mais26)
  tipos = random.choice(sangue) + random.choice(sanguemm)
  persona= random.choice(personalidades)
  await ctx.send(f'`Nome:{random.choice(nomesh)} {random.choice(sobrenomeh)}\nIdade: {idade}\nTipo Sanguíneo: {tipos}\nOcupação: {jobb}\nPersonalidade: {persona}`')


@client.command(aliases=['personagem medieval'])
async def permedi(ctx):
  idade = random.randint(20,60)
  jobb = random.choice(menos25m) if idade <= 25 else random.choice(mais26m)
  tipos = random.choice(sangue) + random.choice(sanguemm)
  persona= random.choice(personalidades)
  await ctx.send(f'`Nome:{random.choice(nomesh)} {random.choice(sobrenomeh)}\nIdade: {idade}\nTipo Sanguíneo: {tipos}\nOcupação: {jobb}\nPersonalidade: {persona}`')

@client.command()
async def maha(ctx):
  await ctx.send(random.choice(mahaa))

@client.command()
async def hug(ctx, user: discord.Member):
  abraçoe = discord.Embed(
    title = f'Olha que fofinhos!',
    description = f'{ctx.author.mention} abraçou {user.mention}',
    color = 2602879
  )

  abraçoe.set_image(url=(random.choice(abraço)))
  
  await ctx.send(f'**{ctx.author.mention} e {user.mention}**')
  await ctx.send(embed = abraçoe)


@client.command()
async def kiss(ctx, user: discord.Member):
  beijoe = discord.Embed(
    title = f'Que isso meu patrão!',
    description = f'{ctx.author.mention} beijou {user.mention}',
    color = 2602879
  )

  beijoe.set_image(url=(random.choice(beijo)))
  
  await ctx.send(f'**{ctx.author.mention} e {user.mention}**')
  await ctx.send(embed = beijoe)


@client.command()
async def eat(ctx, user: discord.Member):
  nanie = discord.Embed(
    title = f'Pode isso, Arnaldo?!',
    description = f'{ctx.author.mention} está fazendo coisas com {user.mention}',
    color = 2602879
  )

  nanie.set_image(url=(random.choice(nani)))
  
  await ctx.send(f'**{ctx.author.mention} e {user.mention}**')
  await ctx.send(embed = nanie)


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

@client.command(aliases=['versão', 'versao', 'ver'])
async def version(ctx):
  await ctx.send(f'Atualmente me encontro na versão {versao}.')

@client.command(aliases=['foto', 'imagem'])
async def avatar(ctx, member: discord.Member):
  show_avatar = discord.Embed(
    title = f'Aqui está a foto dele, senhor {ctx.author}',
    color = 2602879
  )
  show_avatar.set_image(url='{}'.format(member.avatar_url))
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


@client.command()
async def ajuda(ctx):
  await ctx.send(embed = ajuda)


## Erros ##

@avatar.error
async def avatar_handler(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send(f'Alô? Esqueceu de marcar de quem você quer a foto, {ctx.author.mention}!')


@anime.error
async def avatar_handler(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send(f'Tá na Disney, meu querido? Esse comando não existe!')


client.run(key)