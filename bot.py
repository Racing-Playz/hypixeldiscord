#API KEY bd04adbb-7afc-42da-a833-09dbf09fbf06
# bot.py
import discord
import hypixelcustomwrapper
from discord.ext import commands # This is just an extension to make commands a lot easier
import requests

bot = commands.Bot(command_prefix='=') # You can set your prefix to be anything you desire!

botName = "Deagan"

@bot.event
async def on_ready(): # This function will be run by the discord library when the bot has logged in
    print("Logged in as " + botName)
    
    

@bot.command()
async def level(ctx, name): # The name of this function will be the name of the command. 'ctx' just provides context we can use, and all arguments after that are just arguments sent by the command
    level = hypixelcustomwrapper.get_level(name) # This is a reference the function we just created in hypixel.py
    if level is None: # Remember back in hypixel.py we returned 'None' if the API couldn't find a player
        await ctx.send("Player not found! (Make sure to use their **Minecraft** username)") # This just sends a message to the channel the command was sent in from the bot
    else: # We know that we found a player now because level is not None
        await ctx.send(f"Level of user {name}: {level}") # This puts the name and level into the message



@bot.command(name="status")
@commands.cooldown(1, 6, commands.BucketType.user)
async def status(ctx, name):
    onlinestatus = hypixelcustomwrapper.get_session(name)


    if onlinestatus == False:
        await ctx.send("Player not online.")

    else:
        onlinestatus = hypixelcustomwrapper.get_session(name)
        await ctx.send(f"{onlinestatus}")



@status.error
async def cooldown_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


bot.run("NzA3MTI3Njc2NDIyMzI0MjY1.XrP7LQ.S9fd_TtK8mGPL0SJwF6SoBY9kcY") # Replace 'token' with the bot token you generated earlier.