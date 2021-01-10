import time
import discord
# import discord_gui
from discord.ext import commands
import json
import typing
from system import System
import shell
from PIL import Image
import requests
import io
import random

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


# @bot.event
# async def on_message(message):
#     if message.content == "cunnytime" and message.author.id == bot.user.id:
#         for i in range(0, 1000):
#             await message.channel.send("cunny")


@bot.command()
async def info(ctx):
    await ctx.send(f"sender id: {ctx.author.id}")
    await ctx.send(f"owner id: {bot.owner_id}")


@bot.command()
async def ping(ctx, *, member: discord.Member):
    await ctx.send(f"<@{member.id}>")


@bot.command()
async def cum(ctx, member: discord.Member):
    random.seed()
    pic_to_cum = Image.open(requests.get(member.avatar_url_as(format='png', size=512), stream=True).raw)

    cum_images = [
        "https://cdn.discordapp.com/attachments/609378055441612819/619049148062367773/cum-splatter-png-2.png",
        "https://cdn.discordapp.com/attachments/609378055441612819/626884316215115807/fake-cum-png-5-png-image-cum"
        "-transparent-background-369_312.png",
        "https://cdn.discordapp.com/attachments/609378055441612819/626884331322998788/cum-splatter-png-2-300x200.png"]

    cum_image = Image.open(requests.get(cum_images[random.randrange(0, 2)], stream=True).raw)
    region = cum_image.resize((round(pic_to_cum.size[0] * 7/8), round(pic_to_cum.size[1] * 7/8)))
    pic_to_cum.paste(region, (round(pic_to_cum.size[0] * 1/8), round(pic_to_cum.size[1] * 1/8)), region)
    image_binary = io.BytesIO()
    pic_to_cum.save(image_binary, 'PNG')
    image_binary.seek(0)

    await ctx.send(f"you just got CUMMED on BITCH, <@{member.id}> !!!", file=discord.File(fp=image_binary, filename='cum-image.png'))


@bot.command()
@commands.is_owner()
async def ban(ctx, members: commands.Greedy[discord.Member],
              delete_days: typing.Optional[int] = 0, *, reason=None):
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
    await ctx.send(f"b&\nreason: {reason}")


@bot.event
async def on_command_error(ctx, error):
    print(error)

bot.add_cog(System(bot))

# login to either user or bot account
if userbot:
    bot.run(user_token, bot=False)
else:
    bot.run(token)
