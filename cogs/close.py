from discord.ext import commands
import const


class Close(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def close(self, ctx):
        if ctx.author.bot:
            return

        if ctx.channel.category.id != const.CAT_THREAD:
            await ctx.send("You cannot that command use here.")
            return
        elif ctx.channel.topic != f"thread-author: {ctx.author.id}":
            await ctx.send("You don't have permission to use this command.")
            return

        category = self.bot.get_channel(const.CAT_ARCHIVE)
        await ctx.channel.edit(category=category)
        await ctx.send("This thread has closed.")


def setup(bot):
    bot.add_cog(Close(bot))
