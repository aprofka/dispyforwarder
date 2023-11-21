import selfcord
import discord
import datetime
import asyncio
import os
from dotenv import load_dotenv
import yaml

# Store and load the bot tokets safely
load_dotenv()
REAL_BOT_TOKEN = os.getenv("REAL_BOT_TOKEN")
SELF_BOT_TOKEN = os.getenv("SELF_BOT_TOKEN")

# Used to run both bots simultaneously
eventLoop = asyncio.new_event_loop()

# Load YAML data from file
with open('config.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Access the trackedChannels from the loaded YAML data
trackedChannels = yaml_data.get('trackedChannels', {})

def print_with_timestamp(*args, **kwargs):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}]", *args, **kwargs)


# Self-bot (Used to get the messages)
class SelfBot(selfcord.Client):
    async def on_ready(self):
        print_with_timestamp("Logged on as", self.user)

    async def on_message(self, message):
        # This checks if the messages received is from the tracked channels
        if message.channel.id in trackedChannels:
            await realBot.sendMessage(message)


# Actual bot (Used to send the messages)
class RealBot(discord.Client):
    async def on_ready(self):
        print_with_timestamp("Logged on as", self.user)

    async def sendMessage(self, message):
        # Gives the destination and tag data
        channelInfo = trackedChannels[message.channel.id]
        messageContent = f"[{message.author.name}] \n {message.content} \n <@&{channelInfo[1]}>"  # Defaul message without pings

        channel = realBot.get_channel(channelInfo[0])
        await channel.send(
            content=messageContent,
            embeds=message.embeds,
        )
        print_with_timestamp(f"[{message.author.name}]: {message.content[:100]}")

    async def on_message(self, message):
        if message.author == realBot.user:
            # Ignore messages sent by the bot itself
            return

        if message.reference:
            # The message is a reply to another message
            replied_to = await message.channel.fetch_message(message.reference.message_id)
            if replied_to.author == realBot.user:
                # The replied-to message was sent by the bot
                await message.reply("Who asked?")


# Initialize the bots
selfBot = SelfBot()
realBot = RealBot(intents=discord.Intents().all())

# Start the bots
eventLoop.create_task(selfBot.start(SELF_BOT_TOKEN))
eventLoop.create_task(realBot.start(REAL_BOT_TOKEN))
eventLoop.run_forever()
