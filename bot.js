import discord

from hcommands import plevel, pstatus, pfriendcount, pguild, precentgames, pbedwarstats, pduelstats

from discord.ext import commands # This is just an extension to make commands a lot easier
import requests
from datetime import datetime, timezone, timedelta
import json
import time

bot = commands.Bot(command_prefix='=') # You can set your prefix to be anything you desire!

botName = "DisHypixel-Stats"

@bot.event
async def on_ready(): # This function will be run by the discord library when the bot has logged in
    print("Logged in as " + botName)
    
    

@bot.command()
async def level(ctx, name): # The name of this function will be the name of the command. 'ctx' just provides context we can use, and all arguments after that are just arguments sent by the command
    level = plevel.get_level(name) # This is a reference the function we just created in hypixel.py
    if level is None: # Remember back in hypixel.py we returned 'None' if the API couldn't find a player
        await ctx.send("Player not found! (Make sure to use their **Minecraft** username)") # This just sends a message to the channel the command was sent in from the bot
    else: # We know that we found a player now because level is not None
        await ctx.send(f"Level of user {name}: {level}") # This puts the name and level into the message



@bot.command(name="status")
@commands.cooldown(1, 6, commands.BucketType.user)
async def status(ctx, name):
    onlinestatus = pstatus.get_session(name)


    if onlinestatus == False:
        await ctx.send("Player not online.")


    else:
        onlinestatus = pstatus.get_session(name)
        await ctx.send(f"{onlinestatus}")


@bot.command(name="fc")
@commands.cooldown(1, 6, commands.BucketType.user)
async def fc(ctx, name):
    friends_counter = pfriendcount.get_friend_count(name)

    if friends_counter is None:
        return None

    else:
        await ctx.send(f"{friends_counter}")
        
@bot.command(name="guild")
@commands.cooldown(1, 6, commands.BucketType.user)
async def guildinfo(ctx, name):
    pguild_info = pguild.get_guild_info(name)

    if pguild_info is None:
        return None

    else:
        await ctx.send(f"{pguild_info}")

@bot.command(name="recentgames")
@commands.cooldown(1, 6, commands.BucketType.user)
async def recgames(ctx, name):
    regames = precentgames.get_recent_games(name)

    if regames is None:
        return None

    else:
        await ctx.send(f"{regames}")

@bot.command(name="bwstats")
@commands.cooldown(1, 6, commands.BucketType.user)
async def bwstat(ctx, name):
    bw_stat = pbedwarstats.get_bedwars_stats(name)

    if bw_stat is None:
        return None

    else:
        await ctx.send(f"{bw_stat}")

@bot.command(name="duelstats")
@commands.cooldown(1, 6, commands.BucketType.user)
async def bwstat(ctx, name):
    duel_stat = pduelstats.get_duels_stats(name)

    if duel_stat is None:
        return None

    else:
        await ctx.send(f"{duel_stat}")

@status.error
async def cooldown_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


bot.run("NzYwNTcyNDUwNDg3NTMzNjA5.X3OASg.Jip0Qw31xITc9qa5cvwPdX4a_0M") # Replace 'token' with the bot token you generated earlier.
