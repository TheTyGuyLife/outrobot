import discord
from discord.ext import commands
from discord.utils import get
from discord.ext import commands,tasks
import os
from datetime import datetime
from datetime import date
now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")
bot = discord.Client()
@bot.event
async def log(ID,messageauthor,authorimg,context):

  channel = context
  print(channel)

  embed=discord.Embed(title='{} ({})'.format(ID.capitalize(),messageauthor), description='{} called ".{}" at {}'.format(messageauthor,ID,current_time), color=discord.Color.from_rgb(222, 165, 31))
  embed.set_footer(text='requested at {}'.format(today))
  embed.set_thumbnail(url='{}'.format(authorimg))
  await channel.send(embed=embed)
