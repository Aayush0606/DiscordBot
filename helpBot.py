import discord

async def helpBot(message):
    embed=discord.Embed(title="NOOB_BOT Command center",description="Here's a list of all the commands")
    embed.add_field(name="!helloNoob",value="Greet all the server members")
    embed.add_field(name="!helpNoob",value="Show all commands")
    embed.add_field(name="!insultNoob",value="Insult all tagged users")
    embed.add_field(name="!memeNoob",value="Fetch a random meme")
    await message.channel.send(content=None,embed=embed)