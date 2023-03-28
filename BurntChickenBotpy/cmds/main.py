# -*- coding:utf-8 -*-
import discord
from discord.ext import commands
import json
pray = """
**      **      🛐🛐
      🛐            🛐
🛐                        🛐
            🛐🛐
            🛐🛐
      🛐   🛐
         🛐🛐
               🛐
            🛐🛐🛐
"""
class Pong(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Pong Loaded")
    @commands.hybrid_command(name="ping",pass_context=True,discription="Send My Ping")
    async def ping(self,ctx):
        await ctx.send(f"bot.latency= {round(self.bot.latency*1000)}ms")
        return 
    @commands.hybrid_command(name="膜拜",pass_context=True)
    async def place_of_worship(self,ctx):
        with open(file="./data/cmd_useable.json",mode="r",encoding="utf-8") as permission_json:
            permission=json.load(permission_json)
        if(str(ctx.channel.id) in permission["place_of_worship"]["unable"]):
            await ctx.reply("You can't use this command in this guild")
            return
        await ctx.reply(pray)
        return
    @commands.command(name="🛐",description="You are so Dian")
    async def TooDian(self,ctx):
        with open(file="./data/cmd_useable.json",mode="r",encoding="utf-8") as permission_json:
            permission=json.load(permission_json)
        if(str(ctx.channel.id) in permission["place_of_worship"]["unable"]):
            await ctx.reply("You can't use this command in this guild")
            return
        await ctx.send(pray)
        return
    @commands.hybrid_command(name="hi",with_app_command=True,guild=discord.Object(id=1048972316924711003),description="say hello")
    async def ping_command(self, ctx: commands.Context) -> None:
        await ctx.defer()
        await ctx.send(f"Hello! <@{ctx.author.id}> !")


async def setup(bot):
    await bot.add_cog(Pong(bot),guild=discord.Object(id=1020914209795604601))
    print("Main Setup")