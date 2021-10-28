import requests

async def memeBot(message):
    data=requests.get('https://meme-api.herokuapp.com/gimme')
    data=data.json()
    await message.channel.send(data['url'])