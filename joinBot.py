import requests
async def joinBot(member):
    for channel in member.guild.channels:
        if str(channel) == "general": 
            data=requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
            data=data.json()
            await channel.send(f"Welcome homie.Here's your welcome bonus : {data['insult']}  {member.mention}")