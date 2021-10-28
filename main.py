import discord
from discord import message
from discord import embeds
from discord import channel
from greetBot import greetBot
from helpBot import helpBot
from insultBot import insultBot
from joinBot import joinBot
from memeBot import memeBot


token='OTAzMjE1ODA0Nzk4MDk5NDc3.YXpvRA.qqPHNKsYbu3nR_u1mFXB9NkMJ2I'
client=discord.Client()

allowed_mentions = discord.AllowedMentions(everyone = True)
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    
    await joinBot(member)

@client.event
async def on_message(message):
    myServerId=client.get_guild(903215398286143550)
    if message.content.count("!helloNoob")>0:
        await greetBot(message,allowed_mentions)
        
    elif message.content.count("!helpNoob")>0:
        await helpBot(message)

    elif message.content.count("!insultNoob")>0:
        await insultBot(message)
    elif message.content.count("!memeNoob")>0:
        await memeBot(message)



client.run(token)