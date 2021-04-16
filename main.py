import discord
from discord.ext import commands
from discord.utils import get
import discord.ext.commands
import time

intents = discord.Intents()
client = commands.Bot(command_prefix=")",intents = discord.Intents.all())

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
  embed.add_field(name=")commands",value="well its this command duh",inline=False)
  #change channel tags to fit your server
  embed.add_field(name=")poll",value="Parameters: Question. Puts up a poll. Only works in <#829587423235276821>",inline=False)
  embed.add_field(name=")plug",value="Parameters: Channel. Plugs a channel. Only works in <#808770452477837342>", inline=False)
  embed.add_field(name=")react",value="Parameters: MessageID, Emoji. Adds Reaction. Message ID must be the ID of the correct message. To get MessageID, turn on developer mode and right click the message and click \"Copy ID.\" This was made for staff, but we decided to let the public use it.", inline=False)
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

@client.command()
async def react(ctx, MessageID, Emoji):
  await ctx.message.delete()
  try:
    message = await ctx.fetch_message(MessageID)
  except:
    print("nonono")
  if message.channel.id == ctx.channel.id:
    await message.add_reaction(Emoji)

@client.command()
async def amongus(ctx, MessageID):
  await ctx.message.delete()
  print(ctx.author.name)
  try:
    message = await ctx.fetch_message(MessageID)
  except:
    print("nonono")
  if message.channel.id == ctx.channel.id:
    await message.add_reaction("🇦")
    await message.add_reaction("🇲")
    await message.add_reaction("🇴")
    await message.add_reaction("🇳")
    await message.add_reaction("🇬")
    await message.add_reaction("🇺")
    await message.add_reaction("🇸")

@client.command()
async def cheezit(ctx):
  embed = discord.Embed(
    title = "",
    description = "",
    colour = discord.Colour.orange(),
  )
  embed.set_image(url="https://cdn.discordapp.com/attachments/537007354642825236/832326870182789160/AAUvwnjqL_JFeK13c6MyFVm0BpZSvaQNnhzuEvrdTIcvs88-c-k-c0x00ffffff-no-rj.png")
  await ctx.send(embed=embed)
    

#reaction roles
@client.event
async def on_raw_reaction_add(payload):

  message_id = payload.message_id
  if message_id == 831302808682496053:
    print("p")
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g:g.id==guild_id, client.guilds)
    print("weaaaaaaaaaa")
    if payload.emoji.name == "😩":
      role = discord.utils.get(guild.roles, name="Notifications on")
    if payload.emoji.name == "😳":
      role = discord.utils.get(guild.roles, name="Gun")
    if role is not None:
        member = payload.member
        print(member.name)
        if member is not None:  
          await member.add_roles(role)  

@client.event
async def on_raw_reaction_remove(payload):
  message_id = payload.message_id
  if message_id == 831302808682496053:
    print("p")
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g:g.id==guild_id, client.guilds)
    print("weaaaaaaaaaa")
    print(payload.emoji.name)
    role = discord.utils.get(guild.roles, name="Notifications on")
    if payload.emoji.name == "😩":
      role = discord.utils.get(guild.roles, name="Notifications on")
    if payload.emoji.name == "😳":
      role = discord.utils.get(guild.roles, name="Gun")
    if role is not None:
      await discord.utils.get(client.get_all_members(), id = payload.user_id).remove_roles(role)
  
client.run("TOKEN")   
