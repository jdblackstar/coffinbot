import discord
from discord.ext import commands
from discord.utils import get

class Gear(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='update')
    async def update(self, ctx: commands.Context, 
                     family_name: str = None, 
                     char_name: str = None,
                     level: int = None, 
                     AP: int = None, 
                     AAP: int = None, 
                     DP: int = None, 
                     char_class: str = None):
        ...

    @commands.command(name='add')
    async def add(self, ctx: commands.Context, 
                  family_name: str, 
                  char_name: str,
                  level: int, 
                  AP: int, 
                  AAP: int, 
                  DP: int, 
                  char_class: str):
        ...