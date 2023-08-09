# Dispy Forwarder - Discord message forwarding bot

First, keep in mind that self-bots are against Discord's terms of service and are not officially supported by the newest discord modules/plugins. Self-botting could result in your account being banned, so use it with caution. 

## How does it work?
It works by running two bots in the same script simultaneously, the self bot is used to get the messages while the actual/standard bot is used to send the messages. This was done for a few reasons, the first being that, not based on any facts, it would be harder for Discord to detect your self-botting as you never send any messages. Another was that you simply cannot send all the embeds with self-botting, so to combat this we simply let an actual bot do this. 

## Instructions
1. Make sure you have the following installed:
    - Python
    - [Selfcord](https://github.com/dolfies/discord.py-self/tree/renamed)

2. Open bot.py and add your source - target channels as seen in the file to the variable named "trackedChannels".

3. Execute the following in the terminal/console `python bot.py`

*You might need to install some additional libraries/packages
*If you get any errors for missing modules run 'pip install\[PACKAGE-NAME\]'.


## LICENSE

[GNU](LICENSE)
