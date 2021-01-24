from textwrap import dedent

from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send(
            dedent(
                """\
            # Simple Thread は Discord サーバーにスレッド機能を追加する bot です。

            # 使い方
             `/set <ThreadMasterChannel> <ThreadCategory> <ArchiveCategory>`
            スレッドを設定します。

            `<ThreadName>`
            これを `<ThreadMasterChannel>` に送ると、Simple Thread が `<ThreadCategory>` の中に `<ThreadName>` という名前のチャンネルを作成します。

            `/close`
            送信先のスレッドを `<ArchiveCategory>` にアーカイブします。
            
            詳しい使い方は GitHub を読んでください。
            
            # GitHubはこちら
            <https://github.com/tenzyu/simple-quote>

            # サポートサーバーはこちら
            <https://discord.gg/4nSKCE9RRn>
            """
            )
        )


def setup(bot):
    bot.add_cog(Help(bot))
