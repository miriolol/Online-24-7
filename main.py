import keep_alive
import discord
from discord.ext import commands
import os

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    print(f'Logged in as {client.user} ({client.user.id})')


keep_alive.keep_alive()
token = os.environ.get("token")
client.run(token)