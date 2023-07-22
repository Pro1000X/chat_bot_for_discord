import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.content.startswith('!deleteme'):
            msg = await message.channel.send('I will delete myself now...')
            await msg.delete()

            # this also works
            await message.channel.send('Goodbye in 3 seconds...')
            await message.channel.send("JK, i will not delete this message, WKWKWK")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("ur token here")
