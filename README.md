# Dispy Forwarder - Discord message forwarding bot

## Notice

It's important to note that self-bots contravene Discord's terms of service and lack official support from the latest Discord modules/plugins. Engaging in self-botting carries the potential for your account to be banned, making it imperative to exercise caution when considering its use.

## How does it work?

The bot operates by concurrently running two bots within a single script: a self-bot retrieves messages, while an authentic standard bot dispatches messages. This approach was motivated by several considerations. First and foremost, it's hypothesized—albeit without concrete evidence—that Discord's ability to identify self-botting would be diminished, given the absence of message transmission by the self-bot. Furthermore, limitations associated with self-botting prevented the transmission of all embeds. To address this limitation, I opted to delegate the task to a genuine bot.

## The drawbacks

Since the message-sending component operates as a bot, you'll have the capability to only transmit messages to servers where you hold administrative privileges or possess access to an existing approved bot within the designated server.

## Instructions

1. Make sure you have the following installed:

   - [Python3](https://www.python.org/downloads/)
   - [Selfcord](https://github.com/dolfies/discord.py-self/tree/renamed)
   - Pyaml `pip install pyyaml`

2. Open env.example and add configure the channels you want to forward as show inside the file.

3. Change the file env.example to .env

4. Execute the following in the terminal/console `python bot.py` or run the start.bat file

\*You might need to install some additional libraries/packages, so if you get any errors for missing packages run 'pip install \[PACKAGE-NAME\]'.

## LICENSE

[GNU](LICENSE)
