from Magic8.Magic8 import Magic8
from creds import CHANNEL, TOKEN
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.endswith('?') and str(message.channel.id) == CHANNEL:
        magic8 = Magic8(message)
        await magic8.answer_question()

client.run(TOKEN)
