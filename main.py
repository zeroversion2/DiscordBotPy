import time
import discord
# import discord_gui
from discord.ext import commands
import json
import typing
from system import System
import shell

config = open("config.json")
config_data = json.load(config)
token = config_data['token']
user_token = config_data['user_token']
owner = config_data['owner']
prefix = config_data['prefix']
userbot = config_data['userbot']


bot = commands.Bot(command_prefix=prefix, owner_id=owner)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #shell.BotShell().cmdloop()


@bot.command()
async def info(ctx):
    await ctx.send(f"sender id: {ctx.author.id}")
    await ctx.send(f"owner id: {bot.owner_id}")


@bot.command()
async def ping(ctx, *, member: discord.Member):
    await ctx.send(f"<@{member.id}>")


@bot.command()
@commands.is_owner()
async def ban(ctx, members: commands.Greedy[discord.Member],
              delete_days: typing.Optional[int] = 0, *, reason=None):
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
    await ctx.send(f"b&\nreason: {reason}")


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)

bot.add_cog(System(bot))

# login to either user or bot account
if userbot:
    bot.run(user_token, bot=False)
else:
    bot.run(token)
