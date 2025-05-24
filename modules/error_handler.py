import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context
from discord import Interaction
from lists.error_messages import *
import random


class ErrorHandler():
    async def avatar_handler(ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send(f'Alô? Esqueceu de marcar de quem você quer a foto, {ctx.author.mention}!')


    async def avatar_handler(ctx, error):
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            await ctx.send(f'Tá na Disney, meu querido? Esse comando não existe!')

    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(random.choice(error_message))