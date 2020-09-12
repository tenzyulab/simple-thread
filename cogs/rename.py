from discord.ext import commands
import const


class Rename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rename(self, ctx, *, named):
        if ctx.author.bot:
            return

        if (ctx.channel.category == None
                or ctx.channel.category.id != const.CAT_THREAD):
            return
            await ctx.send("You cannot that command use here.")
            return
        elif ctx.channel.topic != f"thread-author: {ctx.author.id}":
            await ctx.send("You don't have permission to use this command.")
            return

        await ctx.channel.edit(name=named)
        await ctx.send(f"{ctx.author.mention} renamed `{named}`")
        return


def setup(bot):
    bot.add_cog(Rename(bot))
