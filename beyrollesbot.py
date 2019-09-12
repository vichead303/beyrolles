import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game('소녀전선')
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await message.channel.send('안녕!!!!!')

    elif message.content.startswith('!say'):
        await message.channel.send('leave message')

access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)

