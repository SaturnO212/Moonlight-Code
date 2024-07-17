import random
from discord.ext import commands
import discord

intent = discord.Intents.all()
randommessages = ["Mhm?", "Yea?", "What's up?"]

client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intent)

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send(random.choice(randommessages))

intents = discord.Intents.all()
intents.message_content = True



@client.command(name='list')
async def _list(ctx, arg):
    await ctx.send(arg)


