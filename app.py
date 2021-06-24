import discord
from discord.ext import commands
from discord import Color
from dotenv import dotenv_values

import Cogs

# Getting Environment Variables
config = dotenv_values(".env")
PREFIX = config["PREFIX"]
TOKEN = config["TOKEN"]

client = commands.Bot(command_prefix = PREFIX)

# Logging When bot starts running
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

# Perform this everytime bot sees a message
@client.event
async def on_message(message):
    if (message.author.bot):
        return
    print(message.content, message.author)
    if (message.content.startswith(PREFIX)):
        await client.process_commands(message)
    else:
        args = message.content.split()
        print(args)

# Other commands
client.add_cog(Cogs.Helper(client, Color.blue()))

# Run the bot
client.run(TOKEN)
