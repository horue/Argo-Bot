import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context
from discord import Interaction
from discord import Embed
from lists.interactions import *
import random



class Interact():
    @staticmethod
    async def hug(ctx, user):
        abraçoe = discord.Embed(
            title = f'Olha que fofinhos!',
            description = f'{ctx.author.mention} abraçou {user.mention}',
            color = 2602879
        )

        abraçoe.set_image(url=(random.choice(Interaction.hug)))
        
        await ctx.send(f'**{ctx.author.mention} e {user.mention}**')
        await ctx.send(embed = abraçoe)

    @staticmethod
    async def kiss(ctx, user):
        beijoe = discord.Embed(
            title = f'Que isso meu patrão!',
            description = f'{ctx.author.mention} beijou {user.mention}',
            color = 2602879
        )

        beijoe.set_image(url=(random.choice(Interaction.kiss)))
        
        await ctx.send(f'**{ctx.author.mention} e {user.mention}**')
        await ctx.send(embed = beijoe)

    @staticmethod
    async def eat(ctx, user):
        nanie = discord.Embed(
            title = f'Pode isso, Arnaldo?!',
            description = f'{ctx.author.mention} está fazendo coisas com {user.mention}',
            color = 2602879
        )

        nanie.set_image(url=(random.choice(Interaction.nani)))
        
        await ctx.send(f'**{ctx.author.mention} e {user.mention}**')
        await ctx.send(embed = nanie)
