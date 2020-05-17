import requests # We also import the maths library because it provides some functions we need
import math
from datetime import datetime, timezone, timedelta
import time

from hmisc import API_KEY

APIKEY = API_KEY.return_api_key()

def get_recent_games(name):
    getUUID = f"https://api.mojang.com/users/profiles/minecraft/{name}"

    res = requests.get(getUUID)
    data = res.json()

    if data["id"] is None:
        return None

    returnUuid = (data["id"])

    getrg = f"https://api.hypixel.net/recentGames?key={APIKEY}&uuid=" + returnUuid

    res2 = requests.get(getrg)
    data2 = res2.json()

    if data2["games"] is None:
        return None

    pgameType = (data2["games"][0]["gameType"])
    pgameMode = (data2["games"][0]["mode"])
    pMap = (data2["games"][0]["map"])

    pgameType2 = (data2["games"][1]["gameType"])
    pgameMode2 = (data2["games"][1]["mode"])
    pMap2 = (data2["games"][1]["map"])

    pgameType3 = (data2["games"][2]["gameType"])
    pgameMode3 = (data2["games"][2]["mode"])
    pMap3 = (data2["games"][2]["map"])

    return "Game: " + "`" + pgameType + "`" + "\n" + "Mode: " + "`" + pgameMode + "`" + "\n" + "Map: " + "`" + pMap + "`" + "\n" + "\n" + "Game: " + "`" + pgameType2 + "`" + "\n" + "Mode: " + "`" + pgameMode2 + "`" + "\n" + "Map: " + "`" + pMap2 + "`" + "\n" + "\n" "Game: " + "`" + pgameType3 + "`" + "\n" + "Mode: " + "`" + pgameMode3 + "`" + "\n" + "Map: " + "`" + pMap3 + "`" + "\n" + "\n"
