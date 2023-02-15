import discord
import os
from dotenv import load_dotenv
from discord.utils import get
import youtube_dl
import pafy
from discord import FFmpegPCMAudio, PCMVolumeTransformer
from filecreation import filecreation
from difflib import SequenceMatcher
from messagechecker import messagechecker
from StatusChecker import statuschecker
from log import log
import asyncio
bot = discord.Client()

#discord.opus.load_opus()
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

intents = discord.Intents.none()
intents.reactions = True
intents.members = True
intents.guilds = True
@bot.event
async def on_voice_state_update(member, before, after):
  if not before.channel and after.channel and member.id == 608415497645457418:
    logchannel = bot.get_channel(1026599731687850045)
    result = statuschecker("Intro")
    if result == False:
        return
    else:
        pass
    await log("intro","NotTy#7025","https://cdn.discordapp.com/avatars/608415497645457418/c0e51977bcd8c64e5f1ca8458baa2b64.webp?size=1024",logchannel)
    filename = "intro.mp4"
    print(before)
    print(member)
    vcchannel = after.channel
    print(vcchannel)
    vc = await vcchannel.connect()
    vc.play(discord.FFmpegPCMAudio(source="./thud.mp4"))
    while vc.is_playing():
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
        while vc.is_playing():
            break
        else:
            await vc.disconnect()
  else:
      pass

  if not before.channel and after.channel and member.id in [677586348739264543,364553357483966468, 727140952564826123, 589895931688910850,699618629930582099]:
    logchannel = bot.get_channel(1026599731687850045)
    result = statuschecker("Fart")
    if result == False:
        return
    else:
        pass
    await log("fart",member.id,"https://miro.medium.com/max/400/1*UL9RWkTUtJlyHW7kGm20hQ.png",logchannel)
    filename = "intro.mp4"
    print(before)
    print(member)
    vcchannel = after.channel
    print(vcchannel)
    vc = await vcchannel.connect()
    vc.play(discord.FFmpegPCMAudio(source="./fart.mp4"))
    while vc.is_playing():
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
        while vc.is_playing():
            break
        else:
            await vc.disconnect()
  else:
      pass
@bot.event
async def on_message(message):
  author = message.author
  avatar = author.avatar_url
  guild = message.guild.name
  guild = '{}.txt'.format(guild)
  channel = message.channel
  messagechannel = channel
  logchannel = bot.get_channel(1026599731687850045)
  try:
    checker = messagechecker(guild, message.content)
    print("checking message")
    await channel.send(checker)

  except Exception as e:
    #print(e)
    pass



  if message.content == ".debug":
      print('test')
      opener = open("./Servers/Bot Development Server (NotTy).txt","w")
      await log("debug",author,avatar,logchannel)
      await channel.send(avatar)
      await channel.send(guild)
      await channel.send(os.listdir("./Servers"))
      #await channel.send(os.listdir("./"))
      #await channel.send(os.environ)
  if message.content == ".outro":
    result = statuschecker("Outro")
    if result == False:
        return
    else:
        pass
    await log("outro",author,avatar,logchannel)
    filename = "outrotrimmed.mp4"
    vcchannel = message.author.voice.channel
    print(vcchannel)
    vc = await vcchannel.connect()
    vc.play(discord.FFmpegPCMAudio(source="./outrotrimmed.mp4"))
    while vc.is_playing():
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(5)
        while vc.is_playing():
            break
        else:
            await vc.disconnect()




token = os.getenv("token")
bot.run(token)
