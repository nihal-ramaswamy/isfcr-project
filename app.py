import discord
from discord.ext import commands
from discord import Color
from dotenv import dotenv_values

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

# Execute !bot_help command
blue = Color.blue()
@client.command()
async def bot_help(ctx):
    embedVar = discord.Embed(title="Help", description="How to use the bot", color=blue)
    embedVar.set_author(name='help')
    embedVar.add_field(name="What do i do?", value="Checks for offensive or abusive \
    language in text, videos, images and links.", inline=False)
    await ctx.send(embed=embedVar)

# Run the bot
client.run(TOKEN)
