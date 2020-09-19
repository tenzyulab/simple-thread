import asyncio
import json
from textwrap import dedent

import discord
from discord.ext import commands

#   This BOT is doing the conversion within that server when the argument is passed,
#   so maybe we don't need to specifically solve the cross-server problem.


class Thread(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        with open("threads.json") as r:
            self.threads = json.load(r)

        self.bot.loop.create_task(self.save_threads())

    async def save_threads(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open("threads.json", "w") as w:
                json.dump(self.threads, w, indent=4)
            await asyncio.sleep(10)

    """
    This is the set command.
    the Server Admins send '/set <ThreadMasterChannel> <ThreadCategory> <ArchiveCategory>'
    Nothing problem, dump these ID to threads.json

    ch_master as ThreadMasterChannel
    cat_thread as ThreadCategory
    cat_archive as ArchiveCategory

    For example: /set 702030388033224714 662856289151615025 702074011772911656
    In Json, Like This
    "702030388033224714": {
        "cat_thread": 662856289151615025,
        "cat_archive": 702074011772911656
    }
    """
    @commands.command(name="set")
    @commands.has_guild_permissions(administrator=True)
    async def _set(self, ctx, ch_master: discord.TextChannel = None, cat_thread: discord.CategoryChannel = None, cat_archive: discord.CategoryChannel = None):
        if ctx.author.bot:
            return

        if not (ch_master and cat_thread and cat_archive):
            embed = discord.Embed(
                title="Tips",
                url="https://github.com/tenzyu/simple-thread",
                description=dedent("""\
                Please send the ID of the ThreadMasterChannel, ThreadCategory and ArchiveCategory; you wanna set to Threader.
                Like this `/set 702030388033224714 662856289151615025 702074011772911656`
                """)
            )
            embed.set_footer(
                text="If you tap the title, jump to the details.")
            await ctx.send(embed=embed)
            return

        ch_master = str(ch_master.id)
        cat_thread = cat_thread.id
        cat_archive = cat_archive.id
        for dict_key in self.threads.keys():
            if ch_master == self.threads[dict_key]:
                await ctx.send("That ThreadMasterChannel is already registered.")
                return
            if cat_thread == self.threads[dict_key]["cat_thread"]:
                await ctx.send("That ThreadCategory is already registered.")
                return
            if cat_archive == self.threads[dict_key]["cat_archive"]:
                await ctx.send("That ArchiveCategory is already registered.")
                return

        self.threads[ch_master] = {}
        self.threads[ch_master]["cat_thread"] = cat_thread
        self.threads[ch_master]["cat_archive"] = cat_archive
        await ctx.send("Registered!")


def setup(bot):
    bot.add_cog(Thread(bot))
