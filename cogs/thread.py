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

    """
    This is the remove command.
    the Server Admins send '/set <ThreadMasterChannel>'
    Nothing problem, pop this Thread of threads.json
    
    ch_master as ThreadMasterChannel

    For example: /remove 702030388033224714
    This Thread of the json file will be popped.
    """
    @commands.command(aliases=["rem"])
    @commands.has_guild_permissions(administrator=True)
    async def remove(self, ctx, ch_master: discord.TextChannel = None):
        if ctx.author.bot:
            return

        if not ch_master:
            embed = discord.Embed(
                title="Tips",
                description=dedent("""\
                Please send the ID of the Thread Master; you wanna remove Thread.
                Like this `/remove 702030388033224714`"""),
                url="https://github.com/tenzyu/simple-thread"
            )
            embed.set_footer(
                text="If you tap the title, jump to the details.")
            await ctx.send(embed=embed)
            return

        ch_master = str(ch_master.id)
        if not ch_master in self.threads:
            await ctx.send("That Thread Master Channel isn't registered.")
            return

        self.threads.pop(ch_master)
        await ctx.send("Removed!")
    
    # From here, the process of sorting by unread order and opening the thread.
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        channel = message.channel

        if not channel.category:
            return

        # Move the thread down one of the ThreadMasterChannel.
        dict_key = str(channel.id)
        if not dict_key in self.threads:
            for dict_key in self.threads.keys():
                if channel.category.id != self.threads[str(dict_key)]["cat_thread"]:
                    continue
                position = self.bot.get_channel(int(dict_key)).position
                if channel.position < position:
                    return
                await channel.edit(position=position + 1)
                return
            return

        # Bring some data
        thread_data = self.threads[dict_key]
        ch_master = int(dict_key)
        cat_thread_id = thread_data["cat_thread"]
        cat_archive_id = thread_data["cat_archive"]

        # If nothing the same name thread, create new thread.
        cat_thread = self.bot.get_channel(cat_thread_id)
        name = message.content.replace(" ", "-").lower()
        thread = discord.utils.get(message.guild.channels, name=name)
        if not thread:
            new_thread = await cat_thread.create_text_channel(name=name)
            await new_thread.edit(topic=f"thread-author: {message.author.id}")
            await new_thread.edit(sync_permissions=True)
            await channel.send(f"{message.author.mention} {new_thread.mention} opened.")
            return

        # If matched the same name thread, show it.
        if thread.category.id == cat_thread_id:
            text = "is already open."
        elif thread.category.id == cat_archive_id:
            text = "is reopened from the archives."
            await thread.edit(topic=f"thread-author: {message.author.id}")
            await thread.edit(category=cat_thread)
            await thread.edit(sync_permissions=True)
        await message.channel.send(f"{message.author.mention} {thread.mention} {text}")

def setup(bot):
    bot.add_cog(Thread(bot))
