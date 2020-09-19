from textwrap import dedent

from discord.ext import commands


class Help(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send(dedent("""\
            **Simple Thread** allows you to add threaded features to your guild.

            > `/set <ThreadMasterChannel> <ThreadCategory> <ArchiveCategory>`
            Setup the Thread to your server.

            > `/remove <ThreadMasterChannel>`
            Remove a Thread containing the `<ThreadMasterChannel>`.

            > `Send a Thread Name to the Thread Master Channel`
            Creates new channel as thread with the name as the message sent in the Thread Category.

            > `/rename <name>`
            If your channel, rename to the `<name>`.
            Note: Due to a limitation on the discord side, the same channel name is updated only twice every 10 minutes.

            > `/close`
            If your channel, move to the Archive Category.
            Tips: Patrol? If you're an administrator, you can close it indiscriminately. Let's keep the server secure!

            > `Sorted by Unread Order`
            Threads below the Thread Master Channel are automatically sorted in unread order.
            Don't mind about which channel is being updated, take a peek at it from above!

            See also GitHub for more information:
            https://github.com/tenzyu/simple-thread
            """))


def setup(bot):
    bot.add_cog(Help(bot))
