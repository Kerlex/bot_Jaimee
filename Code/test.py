import os
import discord
import asyncio

Token = 'NzQxNzEyODg3NTQxNjYxODE2.Xy7j9A.6TbHGMWXQI-MbLxHn6ge7g2wU1g'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        await message.channel.send('Hello!')
        

client = MyClient()
client.run(Token)

