import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('I am on the line!')

    bot_wip_chat = client.get_channel(371323243514298368)

    await bot_wip_chat.send('I am working and online!')

@client.event
async def on_message(message):
    
    if message.content == 'what is the version':
        bot_wip_chat = client.get_channel(371323243514298368)

        await bot_wip_chat.send('the version is 1.0!')

client.run('ODk3OTgwODU5MzE4MTQ1MDQ0.YWdj2A.HtwRPqIviwBJmShJ8ITtPObT7Pk')