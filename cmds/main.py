import discord
from discord.ext import commands
from core.classes import Cog_Extention


class role(Cog_Extention):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        if data.message_id == 1225342647724408862:
            if str(data.emoji) == "☑️":
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(1225342930567434240)
                await data.member.add_roles(role)
                print("1")
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        if data.message_id == 1225342647724408862:
            if str(data.emoji) == "☑️":
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(1225342930567434240)
                await user.remove_roles(role)
                print('123')


async def setup(bot):
    await bot.add_cog(role(bot))
