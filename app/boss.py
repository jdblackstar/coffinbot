# discord imports
import discord
from discord.ext import commands
from discord.utils import get

# timing imports
import time
from datetime import datetime
import asyncio
import async_timeout

class GiveRole(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    '''
    Garmoth
    Karanda
    Kutum
    Kzarka
    Muraka
    Nouver
    Offin
    Quint
    Vell
    '''

    @commands.command()
    async def addroles(self, ctx: commands.Context):
        if get(ctx.guild.roles, name='Garmoth'):
            print('Garmoth role already exists.')
        else:
            await ctx.guild.create_role(name='muted', color=discord.Color('0xff0000'))
            print('muted role created')

class Alert(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='time')
    async def tell_time(self, ctx: commands.Context):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await ctx.send(current_time)