import requests
import math
from datetime import datetime, timezone, timedelta
import time
from hmisc import API_KEY

APIKEY = API_KEY.return_api_key()

def get_guild_info(name):
    getUUID = f"https://api.mojang.com/users/profiles/minecraft/{name}"

    res = requests.get(getUUID)
    data = res.json()

    if data["id"] is None:
        return None

    returnUuid = (data["id"])


    getGUID = f"https://api.hypixel.net/findGuild?key={APIKEY}&byUuid=" + returnUuid

    res2 = requests.get(getGUID)
    data2 = res2.json()

    if data2["guild"] is None:
        return None

    guild_info = (data2["guild"])

    getGinfo = f"https://api.hypixel.net/guild?key={APIKEY}&id=" + guild_info

    res3 = requests.get(getGinfo)
    data3 = res3.json()

    if data3["guild"] is None:
        return None

    guildName = (data3["guild"]["name"])
    guildMembercount = len(data3["guild"]["members"])

    return "Guild Name: " + "`" + guildName + "`" + "\n" + "Members: " + "`" + str(guildMembercount) + "`"

