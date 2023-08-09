import selfcord
import discord
import asyncio

# This is used to run both bots simultaneously
eventLoop = asyncio.new_event_loop()

# Origin/Source Channel ID -> [Target Channel ID, tagType]
trackedChannels = {11111111111111111: [22222222222222222, ""]}


# Self-bot (Used to get the messages)
class SelfBot(selfcord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        # This checks if the messages received is from the tracked channels
        if message.channel.id in trackedChannels:
            await realBot.sendMessage(message)


# Actual bot (Used to send the messages)
class RealBot(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def sendMessage(self, message):
        channelInfo = trackedChannels[message.channel.id]
        channel = realBot.get_channel(channelInfo[0])
        await channel.send(
            content=f"[{message.author.name}] \n {message.content} \n {channelInfo[1]}",
            embeds=message.embeds,
        )


# Initialize the bots
selfBot = SelfBot()
realBot = RealBot(intents=discord.Intents().all())

# Start the bots
eventLoop.create_task(selfBot.start("TOKEN"))
eventLoop.create_task(realBot.start("TOKEN"))
eventLoop.run_forever()
