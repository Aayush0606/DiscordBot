import requests

async def insultBot(message):
    if message.mentions:
        myLst=[]
        for member in message.mentions:
            data=requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
            data=data.json()
            while data['number'] in myLst:
                data=requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
                data=data.json()
            myLst.append(data['number'])
            await message.channel.send(f"{data['insult']} {member.mention}")
    else:
        data=requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
        data=data.json()
        await message.channel.send(f"{data['insult']} {message.author.mention}")