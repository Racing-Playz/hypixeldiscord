# hypixel.py
import requests # We also import the maths library because it provides some functions we need
import math
from datetime import datetime, timezone
import time




API_KEY = "" # Replace with your API key

# These are just values used to calculate the level (don't worry about them too much)
BASE = 10_000
GROWTH = 2_500
REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
REVERSE_CONST = REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2 = 2 / GROWTH



def get_level(name):
    url = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
    res = requests.get(url)
    data = res.json()
    if data["player"] is None:
        return None
    exp = int(data["player"]["networkExp"]) # This just gets the player experience from our data
    return math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * exp)) # This converts Hypixel EXP to a network level



def get_session(name):
    url1 = f"https://api.mojang.com/users/profiles/minecraft/{name}"

    res = requests.get(url1)
    data = res.json()
    if data["id"] is None:
        return None
    returnUuid = (data["id"])

    url2 = f"https://api.hypixel.net/status?key={API_KEY}&uuid=" + returnUuid
    url3 = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"

    res = requests.get(url2)
    res2 = requests.get(url3)
    data = res.json()
    data2 = res2.json()

    if data["session"] is None:
        return None


    if data2["player"] is None:
        return None


    onlinestatus = (data["session"]["online"])


    if onlinestatus is False:
        return False
    else:
        onlinestatus_string = "Online: "
        gameType_string = "Game: "
        gameMode_string = "Mode: "
        lastLogout_string = "LastLogout: "
        lastLogin_string = "LastLogin: "
        newLinestring = "\n"

        game_type = (data["session"]["gameType"])
        game_mode = (data["session"]["mode"])
        log_in = int(data2["player"]["lastLogin"])
        log_out = int(data2["player"]["lastLogout"])
        log_in_converted = timedate = time.strftime('%Y-%m-%d\n%I:%M %p', time.localtime(log_in/1000))
        log_out_converted = timedate = time.strftime('%Y-%m-%d\n%I:%M %p', time.localtime(log_out/1000))
        return onlinestatus_string + "`" + str(onlinestatus) + "`" + newLinestring + gameType_string + "`" + game_type + "`" + newLinestring + gameMode_string + "`" + game_mode + "`" + newLinestring + newLinestring + lastLogin_string + "`" + str(log_in_converted) + "`" + newLinestring + lastLogout_string + "`" + str(log_out_converted) + "`"