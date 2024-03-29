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

## Inazuma Eleven RPG ##

@client.command()
async def passe(ctx, user: discord.Member):
  passebom = random.choice(good_pass)
  await ctx.send(f'{ctx.author.mention} {passebom} {user.mention}')

@client.command()
async def partida(ctx):
  partidaa = random.choice(partidaaa)
  await ctx.send(f'{partidaa}')