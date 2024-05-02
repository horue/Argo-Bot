banner = ('https://imgur.com/H6pKvIH')

good_pass = [
  'consegue efetuar um passe incrível para um companheiro de time!'
]
partidaaa = [
  'O time oponente rouba a bola!',
  'A bola saí! Vantagem do time inimigo.',
  'Um companheiro de time avança mas perde a bola!',
  'A equipe inimiga chega muito perto de marcar um gol mas joga para fora! É tiro de meta!',
  'E é goooool! A equipe inimiga marca um gol incrível!',
  "Goooool! E é gol pra equipe!",
  'Passe feito com sucesso.',
  'Passe oponente feito com sucesso.',
  'Cruzamento para área.',
  'Nas mãos do goleiro!'
]

banners = [
  "https://imgur.com/H6pKvIH"
]


good_pass = [
  'consegue efetuar um passe incrível para um companheiro de time!'
]

## Inazuma Eleven RPG ##

@client.command()
async def passe(ctx, user: discord.Member):
  passebom = random.choice(good_pass)
  await ctx.send(f'{ctx.author.mention} {passebom} {user.mention}')

@client.command()
async def partida(ctx):
  partidaa = random.choice(partidaaa)
  await ctx.send(f'{partidaa}')

## SAO ##

@client.command()
async def eventos(ctx):
  await ctx.send(f'O evento atual é: {banner}')

##General Stuff##
  
@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name = '╚ Soldado')
  await client.add_roles(member, role)


## Batalha ##

@client.command()
async def farm(ctx):
  await ctx.send(f'Um {random.choice(bichos)} apareceu! O que deseja fazer?\nAtacar\nDefender\nFugir')
  msg = await client.wait_for('escolha')
  attempt = int(msg.content)
  if attempt == 'Atacar':
    await ctx.send('Você causou X de dano!')
        

