import selfcord
import discord
import datetime
import asyncio
import os
from dotenv import load_dotenv

# This will allow us to store and load the bot tokets safely
load_dotenv()
REAL_BOT_TOKEN = os.getenv("REAL_BOT_TOKEN")
SELF_BOT_TOKEN = os.getenv("SELF_BOT_TOKEN")

# This is used to run both bots simultaneously
eventLoop = asyncio.new_event_loop()

# Origin/Source Channel -> [Target Channel, tagType]
trackedChannels = {1111111111111111: [2222222222222, "@here"]}


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
        channelInfo = trackedChannels[message.channel.id]
        channel = realBot.get_channel(channelInfo[0])
        await channel.send(
            content=f"[{message.author.name}] \n {message.content} \n {channelInfo[1]}",
            embeds=message.embeds,
        )
        print_with_timestamp(f"[{message.author.name}]: {message.content[:100]}")


# Initialize the bots
selfBot = SelfBot()
realBot = RealBot(intents=discord.Intents().all())

# Start the bots
eventLoop.create_task(selfBot.start(SELF_BOT_TOKEN))
eventLoop.create_task(realBot.start(REAL_BOT_TOKEN))
eventLoop.run_forever()
