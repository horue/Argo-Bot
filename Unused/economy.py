

## Economia ##


@client.command()
async def carteira(ctx, user: discord.Member):
  await open_account(user)
  user = ctx.author
  users = await get_bank_data()

  carteira_quantidade = users[str(user.id)]["carteira"]
  banco_quantidade = users[str(user.id)]["banco"]

  wallet = discord.Embed(
    title = f'Dinheiro de {ctx.author.name}',
    description = 'Aqui estão suas informações bancárias:',
    color = 2602879
  )

  wallet.add_field(name = "Carteira:", value = carteira_quantidade)
  wallet.add_field(name = "Banco:", value = banco_quantidade)



  await ctx.send(embed = wallet)


@client.command()
async def pedir(ctx):
  await open_account(ctx.author)

  users = await get_bank_data()

  user = ctx.author

  earnings = random.randrange(100, 500)

  await ctx.send(f"Você achou {earnings} no chão!")

  users[str(user.id)]["carteira"] += earnings

  with open("mainbank.json","w") as f:
    json.dump(users,f)

async def open_account(user):
 
  users = await get_bank_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["carteira"] = 0
    users[str(user.id)]["banco"] = 0

  with open("mainbank.json","w") as f:
    json.dump(users,f)
  return True


async def get_bank_data():
  with open("mainbank.json","r") as f:
    users = json.load(f)

  return users

