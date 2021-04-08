import discord
from discord.ext import commands
from discord.utils import get
import discord.ext.commands
import time

client = commands.Bot(command_prefix=")")

@client.event
async def on_ready():
    print("Bot is online")

@client.command()
async def commands(ctx):
  embed = discord.Embed(
    title = "List of Commands",
    description = "(all except the secret ones hehehe)",
    colour = discord.Colour.orange(),
  )
  embed.add_field(name="commands",value="well its this command duh",inline=False)
  #change channel tags to fit your server
  embed.add_field(name="poll",value="Parameters: Question. Puts up a poll. Only works in <#829587423235276821>",inline=False)
  embed.add_field(name="plug",value="Parameters: Channel. Plugs a channel. Only works in <#808770452477837342>", inline=False)
  await ctx.send(embed=embed)


@client.command()
async def plug(ctx, *,channel):
  #if you want to use this command in your server, make sure that "🙌-promotion" in the following line is the name of the promtion channel in your server, or if you want the ability to send promotions in every channel, remove this if statement and the else statement (along with the else statement's code)
  if str(ctx.channel) == "🙌-promotion":
    await ctx.message.delete()
    if channel == "":
      return
    await ctx.send("Make sure to sub/follow " + channel + " (from: " + ctx.author.mention + ")")
  else:
    await ctx.message.delete()
    print("wrong channel for promotion")
  

@client.command()
async def poll(ctx, *, question):
  #if you want to use this command in your server, make sure that "🗳-polls" in the following line is the name of the polls channel in your server, or if you want the ability to make polls in every channel, remove this if statement and the else statement (along with the else statement's code)
  await ctx.message.delete()
  if question == "":
    return
  if str(ctx.channel) == "🗳-polls":
    print("poll question asked")
    splitMsg = [char for char in question]
    if "?" not in splitMsg:
      splitMsg.append("?")
    username = ctx.message.author.name
    splitMsg.append(" (from: " + username + ")")
    a = ""
    for i in splitMsg:
      a += i
    msg = await ctx.send(a)
    await msg.add_reaction("✅")
    await msg.add_reaction("❎")
    print("poll reactions added")
  else:
    await ctx.message.delete()
    print("poll asked in incorrect channel")
  
client.run("TOKEN")   
