# hypixel.py
import requests # We also import the maths library because it provides some functions we need
import math




API_KEY = "bd04adbb-7afc-42da-a833-09dbf09fbf06" # Replace with your API key

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
    url3 = f"https://api.hypixel.net/player?key={API_KEY}&uuid=" + returnUuid

    res = requests.get(url2)
    data = res.json()
    if data["session"] is None:
        return None


    onlinestatus = (data["session"]["online"])


    if onlinestatus is None:
        return None
    else:
        return onlinestatus






def get_gametype(name):
    url1 = f"https://api.mojang.com/users/profiles/minecraft/{name}"

    res = requests.get(url1)
    data = res.json()
    if data["id"] is None:
        return None
    returnUuid = (data["id"])

    url2 = f"https://api.hypixel.net/status?key={API_KEY}&uuid=" + returnUuid

    res = requests.get(url2)
    data = res.json()
    if data["session"] is None:
        return None

    game_type = (data["session"]["gameType"])

    if game_type is None:
        return None

    else:
        return game_type


def get_gamemode(name):
    url1 = f"https://api.mojang.com/users/profiles/minecraft/{name}"

    res = requests.get(url1)
    data = res.json()
    if data["id"] is None:
        return None
    returnUuid = (data["id"])

    url2 = f"https://api.hypixel.net/status?key={API_KEY}&uuid=" + returnUuid

    res = requests.get(url2)
    data = res.json()
    if data["session"] is None:
        return None

    game_mode = (data["session"]["mode"])

    if game_mode is None:
        return None

    else:
        return game_mode





