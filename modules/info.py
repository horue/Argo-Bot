from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context
from discord import Interaction

log_file = open("change.log", 'r', encoding='utf-8').read()
versao = ('0.1.0')


class Info():
    @staticmethod
    async def log(ctx):
        try:
            await ctx.send(log_file)
        except:
            await ctx.send('Ops! Algum erro ocorreu enquanto eu tentava te mandar as novidades! Tenta de novo mais tarde!')

    @staticmethod
    async def servidor(ctx):
        await ctx.send(f'Sinta-se livre para entrar no meu servidor oficial, {ctx.author.mention}!\nAqui está o link: https://discord.gg/t2HBP7q37s')

    @staticmethod
    async def version(ctx):
        await ctx.send(f'Atualmente me encontro na versão {versao}.')

    @staticmethod
    async def l(ctx):
        await ctx.send("I lived, Bithces.")