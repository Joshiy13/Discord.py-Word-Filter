from tokenize import Token
import discord
import os

token = os.getenv('TOKEN')
client = discord.Client()


with open("banned.txt") as file: 
    banned = [banned.strip().lower() for banned in file.readlines()]


@client.event 
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(ctx):
  message=ctx.content
  messagelower=message.lower()
  if any(x in messagelower for x in banned):
    await ctx.delete()


client.run(token)