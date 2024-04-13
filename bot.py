import discord
from discord.ext import commands
import os
import tweepy

# 機器人權限
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# 啟動機器人


class MyHelp(commands.HelpCommand):
   # !help
    async def send_bot_help(self, mapping):
        await self.context.send("")


bot.help_command = MyHelp()


@bot.event
async def on_ready():
    for filename in os.listdir("./cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
    print("Bot is Online")

# 歡迎/退出訊息


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1224695912383905893)
    await channel.send(f"歡迎{member.mention}加入伺服器!")


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1224695912383905893)
    await channel.send(f"我們懷念{member.mention}")

    # 載入指令


@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"loaded {extension}")


@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"unloaded {extension}")


@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"reloaded {extension}")


# 防止讀取main時重複執行
if __name__ == "__main__":
    bot.run("MTIyNDcwNDQ4MjQ2MjUzMTYxNQ.G2p7X_.pITitgpE1uvOypRu0uD3AMp5mL9hXfGclMXfPU")
