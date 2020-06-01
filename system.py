import discord
from discord.ext import commands
import time


class System(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    async def cog_check(self, ctx):
        pass

    @commands.command()
    async def create_server(self, ctx, *, name: str):
        server = await self.bot.create_guild(name)
        await ctx.send(f"server {server.name} created with id {server.id}")
        #time.sleep(1)
        invite = await self.bot.get_guild(server.id).system_channel.create_invite()
        await ctx.send(f"invite: {invite.url}")

    @commands.command()
    async def list_servers(self, ctx):
        await ctx.send('```\n' +
                       '\n'.join([f"{guild.name}: {guild.id}, {guild.member_count} members" for guild in self.bot.guilds])
                       + '\n```')
        print(self.bot.guilds)

    @commands.command()
    async def delete_server(self, ctx, guild_id: int = None):
        server = None
        user = ctx.author
        if guild_id:
            server = self.bot.get_guild(guild_id)
        else:
            server = ctx.guild

        await ctx.send(f"deleting server {server.name} in 5...")
        time.sleep(1)
        await ctx.send("4...")
        time.sleep(1)
        await ctx.send("3...")
        time.sleep(1)
        await ctx.send("2...")
        time.sleep(1)
        await ctx.send("1...")
        time.sleep(1)

        await server.delete()

        message = f"deleted server {server.name} :thumbsup:"

        try:
            await ctx.send(message)
        except discord.errors.NotFound:
            await user.send(message)

    @commands.command()
    async def give_admin(self, ctx):
        role = await ctx.guild.create_role(name="admin", permissions=discord.Permissions(8))
        await ctx.author.add_roles(role)

    @commands.command()
    async def give_owner(self, ctx):
        await ctx.guild.edit(owner=ctx.author)

    @commands.command()
    async def give_invite(self, ctx, guild_id: int):
        invite = await self.bot.get_guild(guild_id).system_channel.create_invite()
        await ctx.author.send(invite.url)
