import asyncio
import json
from textwrap import dedent

import discord
from discord.ext import commands


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


def setup(bot):
    bot.add_cog(Thread(bot))
