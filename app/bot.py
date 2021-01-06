# base imports
import os
from dotenv import load_dotenv
import random
import math
import functools
import itertools
import asyncio
import json

# cron imports
import croniter
import aiocron

# discord imports
import discord
from discord.ext import commands
from discord.utils import get


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

##############################
##### SET COMMAND SYNTAX #####
##############################

bot = commands.Bot('.', description='don\'t say uwu')

####################
##### ADD COGS #####
####################

# maybe put module imports here too
from general import General
bot.add_cog(General(bot))

from boss import Alert
bot.add_cog(Alert(bot))

###############################
##### EVENTS FOR TERMINAL #####
###############################

@bot.event
async def on_ready():
    print('Logged in as: \n{0.user.name}\n{0.user.id}'.format(bot))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

###################
##### RUN BOT #####
###################


# tests sending a message every 1 minute to the #gearscore channel
# @aiocron.crontab('*/1 * * * *')
# async def crontest():
#     channel = bot.get_channel(708190271225069568)
#     await channel.send('Sending a message every 1 minute.')

bot.run(TOKEN)