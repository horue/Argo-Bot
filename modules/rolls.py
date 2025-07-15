import random
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context
from discord import Interaction


class Dice():
    async def roll(ctx, info, conta='', ficha=''):
        quantidade, numero = info.split('d')
        nquantidade = int(quantidade)
        if nquantidade > 1:
            resultados=[]
            for i in range (nquantidade):
                rolagem=random.randint(1,int(numero))
                resultados.append(rolagem)
            await ctx.send(f'{ctx.author.mention} 🎇 \n**Rolagem de**: {quantidade}d{numero}\n**Total**: {sum(resultados)}\n**Resultados**: {resultados}')
        else:
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


    async def multiroll(ctx, quantidade=1, numero=20):
        resultados=[]
        for i in range (quantidade):
            rolagem=random.randint(1,int(numero))
            resultados.append(rolagem)
        await ctx.send(f'{ctx.author.mention} 🎇 \n**Rolagem de**: {quantidade}d{numero}\n**Resultados**: {resultados}')


class Coin():
    async def moeda(ctx):
        result = random.randint(0,1)
        await ctx.send('E o resultado é...')
        await ctx.send('...')
        if result == 0:
            return('Cara!')
        elif result == 1:
             return('Coroa!')