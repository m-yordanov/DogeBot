import discord
from discord.ext.commands import Bot
from discord.ext import commands
import wikipediaapi
import random
from random import randrange
import os
import requests
import json
import asyncio
import aiohttp
from keep_alive import keep_alive
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import wikipediaapi
import random
from random import randrange
import os
import requests
import json
import asyncio
import aiohttp
from keep_alive import keep_alive

bot = discord.ext.commands.Bot(command_prefix=['='], help_command = None, intents=discord.Intents.all())

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name='Your nudes', url='https://www.twitch.tv/random_e%27)'))
  print('We have logged in as {0.user}'.format(bot))

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
     
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Commands list", description="", color=0xFEDA30)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="=wiki", value="Sends the summary of a wiki article about the search query.", inline=True)
    embed.add_field(name="=inspire", value="Sends an inspiration quote.", inline=False)
    embed.add_field(name="=coinflip", value="Flips a coin.", inline=False)
    embed.add_field(name="=dog", value="Sends a picture of a dog along with a random fact about dogs.", inline=False)
    embed.add_field(name="=cat", value="Sends a picture of a cat along with a random fact about cats.", inline=False)
    embed.add_field(name="=ping", value="Responds with pong.", inline=False)
    embed.add_field(name="=clear (number)", value="Clears the given amount of messages in the channel.", inline=False)
    embed.add_field(name="=slowmode (seconds)", value="Puts the channel on slowmode for the selected seconds.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def inspire(ctx):
   quote = get_quote()
   await ctx.channel.send(quote)

@bot.command()
async def ping(ctx, args='Pong'):
    await ctx.send(args)

@bot.command()
@commands.has_role('Admin')
async def clear(ctx, amount=100):
  await ctx.channel.purge(limit=amount)

@bot.command()
async def wiki(ctx, *query):
    if query:
         query = " ".join(query)
         wiki_wiki = wikipediaapi.Wikipedia('en')
         page_py = wiki_wiki.page(query)
         page_finished = str(page_py.summary[:1800])
         if not page_finished:
           await ctx.send("Could not find a page.")
         else:
           embed = discord.Embed(title=page_py.title, url=page_py.fullurl, description=page_finished, color=0xFEDA30) 
           if page_finished.endswith("."):
            embed = discord.Embed(title=page_py.title, url=page_py.fullurl, description=page_finished, color=0xFEDA30) 
           else:
            embed = discord.Embed(title=page_py.title, url=page_py.fullurl, description=page_finished + "...", color=0xFEDA30) 
           await ctx.send(embed=embed)
    else:
      await ctx.send("You need to input what page you're looking for!")
  
#@bot.command()
#async def servers(ctx):
  #await ctx.send('\n'.join(guild.name for guild in bot.guilds))
  
@bot.command()
@commands.has_role('Moderator')
async def slowmode(ctx, seconds:int):
  await ctx.channel.edit(slowmode_delay=seconds)

@bot.command(Pass_context=True, aliases=['flip', 'testing'])
async def coinflip(ctx):
    variable = ["heads", "tails"]
    flip = random.choice(variable)
    await ctx.send(flip)   

@bot.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()

      request2 = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request2.json()

   embed = discord.Embed(title="Doggo!", color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat')
      dogjson = await request.json()

      request2 = await session.get('https://some-random-api.ml/facts/cat')
      factjson = await request2.json()

   embed = discord.Embed(title="Cat!", color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
    
  await bot.process_commands(message)
  
keep_alive()
bot.run(os.getenv('TOKEN'))
bot = discord.ext.commands.Bot(command_prefix=['='], help_command = None, intents=discord.Intents.all())import discord
from discord.ext.commands import Bot
from discord.ext import commands
import wikipediaapi
import random
from random import randrange
import os
import requests
import json
import asyncio
import aiohttp
from keep_alive import keep_alive

bot = discord.ext.commands.Bot(command_prefix=['='], help_command = None, intents=discord.Intents.all())

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name='Your nudes', url='https://www.twitch.tv/random_e%27)'))
  print('We have logged in as {0.user}'.format(bot))

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
     
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description="Here is the list with commands:", color=0xFEDA30)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="=wiki", value="Sends the summary of a wiki article about the search query.", inline=True)
    embed.add_field(name="=inspire", value="Sends an inspiration quote.", inline=False)
    embed.add_field(name="=coinflip", value="Flips a coin.", inline=False)
    embed.add_field(name="=dogfact", value="Tells a random fact about dogs.", inline=False)
    embed.add_field(name="=catfact", value="Tells a random fact about cats", inline=False)
    embed.add_field(name="=ping", value="Responds with pong.", inline=False)
    embed.add_field(name="=clear (number)", value="Clears the given amount of messages in the channel.", inline=False)
    embed.add_field(name="=slowmode (seconds)", value="Puts the channel on slowmode for the selected seconds.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def inspire(ctx):
   quote = get_quote()
   await ctx.channel.send(quote)

@bot.command()
async def ping(ctx, args='Pong'):
    await ctx.send(args)

@bot.command()
@commands.has_role('Admin')
async def clear(ctx, amount=100):
  await ctx.channel.purge(limit=amount)

@bot.command()
async def wiki(ctx, *query):
    if query:
         query = " ".join(query)
         wiki_wiki = wikipediaapi.Wikipedia('en')
         page_py = wiki_wiki.page(query)
         page_finished = str(page_py.summary[:1800])
         if not page_finished:
           await ctx.send("Could not find a page.")
         else:
           embed = discord.Embed(title=page_py.title, url=page_py.fullurl, description=page_finished, color=0xFEDA30) 
           if page_finished.endswith("."):
            embed = discord.Embed(title=page_py.title, url=page_py.fullurl, description=page_finished, color=0xFEDA30) 
           else:
            embed = discord.Embed(title=page_py.title, url=page_py.fullurl, description=page_finished + "...", color=0xFEDA30) 
           await ctx.send(embed=embed)
    else:
      await ctx.send("You need to input what page you're looking for!")

#This command is for checking the servers the bot is in
#@bot.command()
#async def servers(ctx):
  #await ctx.send('\n'.join(guild.name for guild in bot.guilds))
  
@bot.command()
@commands.has_role('Moderator')
async def slowmode(ctx, seconds:int):
  await ctx.channel.edit(slowmode_delay=seconds)

@bot.command(Pass_context=True, aliases=['flip', 'testing'])
async def coinflip(ctx):
    variable = ["heads", "tails"]
    flip = random.choice(variable)
    await ctx.send(flip)   

@bot.command()
async def dogfact(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request.json()
   await ctx.send(factjson['fact'])

@bot.command()
async def catfact(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/facts/cat')
      factjson = await request.json()
   await ctx.send(factjson['fact'])

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
    
  await bot.process_commands(message)
  
keep_alive()
bot.run(os.getenv('TOKEN'))

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name='Your nudes', url='https://www.twitch.tv/random_e%27)'))
  print('We have logged in as {0.user}'.format(bot))

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@bot.command()
async def inspire(ctx):
   quote = get_quote()
   await ctx.channel.send(quote)
      
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description="Here is the list with commands:", color=0xFEDA30)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.add_field(name="=wiki", value="Sends the summary of a wiki article about the search query.", inline=True)
    embed.add_field(name="=inspire", value="Sends an inspiration quote.", inline=False)
    embed.add_field(name="=coinflip", value="Flips a coin.", inline=False)
    embed.add_field(name="=dogfact", value="Tells a random fact about dogs.", inline=False)
    embed.add_field(name="=catfact", value="Tells a random fact about cats", inline=False)
    embed.add_field(name="=ping", value="Responds with pong.", inline=False)
    embed.add_field(name="=clear (number)", value="Clears the given amount of messages in the channel.", inline=False)
    embed.add_field(name="=slowmode (seconds)", value="Puts the channel on slowmode for the selected seconds.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx, args='Pong'):
    await ctx.send(args)

@bot.command()
@commands.has_role('Admin')
async def clear(ctx, amount=100):
  await ctx.channel.purge(limit=amount)

bad_words = ["test", "panic", "five"]

@bot.command()
async def wiki(ctx, *query):
    if query:
         query = " ".join(query)
         wiki_wiki = wikipediaapi.Wikipedia('en')
         page_py = wiki_wiki.page(query)
         page_finished = str(page_py.summary[:1800])
         embed = discord.Embed(title=page_py.title, url=page_py.fullurl, description=page_finished, color=0xFEDA30) 
         if page_finished.endswith("."):
          embed = discord.Embed(title=page_py.title, url=page_py.fullurl, description=page_finished, color=0xFEDA30) 
         else:
          embed = discord.Embed(title=page_py.title, url=page_py.fullurl, description=page_finished + "...", color=0xFEDA30) 
         await ctx.send(embed=embed)

#@bot.command()
#async def servers(ctx):
  #await ctx.send('\n'.join(guild.name for guild in bot.guilds))
  
@bot.command()
@commands.has_role('Moderator')
async def slowmode(ctx, seconds:int):
  await ctx.channel.edit(slowmode_delay=seconds)

@bot.command(Pass_context=True, aliases=['flip', 'testing'])
async def coinflip(ctx):
    variable = ["heads", "tails"]
    flip = random.choice(variable)
    await ctx.send(flip)   

@bot.command()
async def dogfact(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request.json()
   await ctx.send(factjson['fact'])

@bot.command()
async def catfact(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/facts/cat')
      factjson = await request.json()
   await ctx.send(factjson['fact'])

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
    
  await bot.process_commands(message)
  
keep_alive()
bot.run(os.getenv('TOKEN'))
