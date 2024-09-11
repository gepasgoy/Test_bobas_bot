from disnake.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Работает, полёт нормальный")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "nice":
            await message.channel.send("for real")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hiiii! :3")


def setup(bot):
    bot.add_cog(Test(bot))
