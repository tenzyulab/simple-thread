from textwrap import dedent

from discord.ext import commands


class Help(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send(
            dedent(
                """\
            **Simple Thread** allows you to add threaded features to your guild.

            > `/set <ThreadMasterChannel> <ThreadCategory> <ArchiveCategory>`
            Sets the Thread to your server.

            > `/remove <ThreadMasterChannel>`
            Removes the saved Thread features with the set command.

            > `<ThreadName>`
            When you send it to `<ThreadMasterChannel>`, Simple Thread creates a new channel named `<ThreadName>` in `<ThreadCategory>`.

            > `/close`
            When you send it to closed channel in `<ArchiveCategory>`, it is reopened.
            
            > `/rename <name>`
            Renames the channel to `<ThreadName>` only if sent to your channel by you.

            > `/close`
            Archives the channel to `<ArchiveCategory>` only if sent to your channel by you.

            See also GitHub for more information:
            https://github.com/tenzyu/simple-thread
            """
            )
        )


def setup(bot):
    bot.add_cog(Help(bot))
