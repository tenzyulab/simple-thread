from discord.ext import commands
import discord
import const


class Open(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if (message.author.bot
                or message.channel.category.id != const.CAT_THREAD):
            return

        if message.channel.id != const.CH_MASTER:
            position = self.bot.get_channel(const.CH_MASTER).position + 2
            await message.channel.edit(position=position)
            return

        name = message.content
        cat_thread = self.bot.get_channel(const.CAT_THREAD)
        response = discord.utils.get(message.guild.channels, name=name)
        if not response:
            new_thread = await cat_thread.create_text_channel(name=name)
            await new_thread.edit(topic=f"thread-author: {message.author.id}")
            await message.channel.send(f"{message.author.mention} {new_thread.mention} opened.")
            return

        if response.category.id == const.CAT_THREAD:
            text = "has already opened."
        elif response.category.id == const.CAT_ARCHIVE:
            text = "has reopened from archives."
            await response.edit(topic="thread-author: " + str(message.author.id))
            await response.edit(category=cat_thread)
        await message.channel.send(f"{message.author.mention} {response.mention} {text}")


def setup(bot):
    bot.add_cog(Open(bot))
