# Glambot by xXwazerzXx

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='g/')

@bot.event
async def on_ready():
    print ("Ready when you are")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!")

@bot.command(pass_context=True)
async def upload(ctx):
    await bot.say("This is Glams Newest Upload: https://www.youtube.com/watch?v=v3VZ6Ix8tSY&feature=youtu.be.")

@bot.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here is the info I could find.", color=0x4286f4)
    embed.set_author(name="Infomation")
    embed.add_field(name="Name", value =ctx.message.server.name)
    embed.add_field(name="Owner", value =ctx.message.server.owner)
    embed.add_field(name="Youtube Channel", value =("GlamPlays: https://www.youtube.com/user/glamplays"))
    embed.add_field(name="Roles", value=len(ctx.message.server.roles))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Bot Creator", value=("xXwazerzXx#2122"))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def faq(ctx):
    embed = discord.Embed(name="{}'s faq".format(ctx.message.server.name), description="Here are Question's Glam gets Asked.", color=0x4286f4)
    embed.set_author(name="FAQ")
    embed.add_field(name="What is your channel?", value =("GlamPlays."))
    embed.add_field(name="Will you play with us?", value =("Maybe"))
    embed.add_field(name="What dogs do you like?", value =("My dog, Honey."))
    embed.add_field(name="What is your favorite game?", value =("Minecraft or Portal 2"))
    embed.add_field(name="What is your real name?", value =("You'll never know :wink:."))
    embed.add_field(name="How do I apply for staff?", value =("#apply-for-staff chat!"))
    embed.add_field(name="Is Swearing Allowed?", value =("#rules chat!"))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def clear(ctx, number):
    mgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)

@bot.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    await bot.say(":hugging: {} just got hugged! https://cdn.discordapp.com/attachments/452098407205699599/452950096259317770/giphy.gif".format(user.name))
    
@bot.command(pass_context=True)
async def slap(ctx, user: discord.Member):
    await bot.say(":clap: {} just got slapped! https://cdn.discordapp.com/attachments/452098407205699599/452953938434588673/giphy_1.gif".format(user.name))


bot.run("NDUyMTA5MzQ5Nzg4MTg4Njgz.DfLjNw.t68VZSe0Rqr813zX4_QXGhmpbgg")
