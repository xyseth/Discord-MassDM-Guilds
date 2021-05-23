import discord
import discord.ext
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style
import time
import asyncio
client = commands.Bot(command_prefix=".", self_bot=True)

seth = client
@seth.event
async def on_connect():
  print(f"{Fore.GREEN} Connected to {seth.user}")

@seth.command()
async def dmall(ctx, *, message):
    i = 1
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(0.5)
            print(f"{Fore.RED}Sleeping For 0.5 Second")
            await user.send(message)
            print(f"{Fore.GREEN}Sent {seth.member}: {message}")
            print(f"{Fore.GREEN}Successfully MassDMED {Fore.RESET}{i}")
            i =+ 1  
        except:
            print(f"{Fore.RED}Couldn't Dmall {seth.id}")
            pass

seth.run("token", bot=False)
