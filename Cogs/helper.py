import discord
from discord.ext import commands

""""
    Prints all the functional features of the bot.
"""

class Helper(commands.Cog):
    def __init__(self, bot, color):
        self.bot = bot
        self.color = color

    @commands.command()
    async def whoareu(self, ctx):
        """Prints what the bot does"""
        embedVar = discord.Embed(title="Help", description="How to use the bot", color=self.color)
        embedVar.set_author(name='help')
        embedVar.add_field(name="What do i do?", value="I check for offensive and NSFW content.", inline=False)
        await ctx.send(embed=embedVar)
