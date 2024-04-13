import discord
from discord.ext import commands
from core.classes import Cog_Extention

class role(Cog_Extention):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tweet(self,)