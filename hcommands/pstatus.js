import requests # We also import the maths library because it provides some functions we need
import math
from datetime import datetime, timezone, timedelta
import time

from hmisc import API_KEY
from hmisc import pcache

APIKEY = API_KEY.return_api_key()

def get_session(name):
    url1 = f"https://api.mojang.com/users/profiles/minecraft/{name}"

    res = requests.get(url1)
    data = res.json()
    if data["id"] is None:
        return None
    returnUuid = (data["id"])

    url2 = f"https://api.hypixel.net/status?key={APIKEY}&uuid=" + returnUuid
    url3 = f"https://api.hypixel.net/player?key={APIKEY}&name={name}"
    url4 = f"https://api.hypixel.net/recentGames?key={APIKEY}&uuid=" + returnUuid

    res = requests.get(url2)
    res2 = requests.get(url3)
    res3 = requests.get(url4)

    data = res.json()
    data2 = res2.json()
    data3 = res3.json()

    if data["session"] is None:
        return None

    if data2["player"] is None:
        return None

    onlinestatus = (data["session"]["online"])

    if onlinestatus is False:
        theNewLineString = "\n"
        lastLogout_string = "LastLogout: "
        log_out = int(data2["player"]["lastLogout"])

        timenow = datetime.now()
        
        log_out_converted = time.strftime('%Y-%m-%d %I:%M %p', time.localtime(log_out / 1000))
        diff = timenow - datetime.strptime(log_out_converted, '%Y-%m-%d\n%I:%M %p')

        diff2 = timenow - datetime.strptime(log_out_converted, '%Y-%m-%d\n%I:%M %p')

        # diff = log_out_converted - log_in_converted
        return str("Online: ") + "`" + "False" + "`" + theNewLineString + theNewLineString + lastLogout_string + "`" + log_out_converted + theNewLineString + "`"

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
        last_game_ended = int(data3["games"][0]["ended"])

        last_game_ended_converted = timedate = time.strftime('%Y-%m-%d\n%I:%M %p', time.localtime(last_game_ended / 1000))

        log_in_converted = timedate = time.strftime('%Y-%m-%d\n%I:%M %p', time.localtime(log_in / 1000))
        log_out_converted = timedate = time.strftime('%Y-%m-%d\n%I:%M %p', time.localtime(log_out / 1000))



        return onlinestatus_string + "`" + str(onlinestatus) + "`" + newLinestring + gameType_string + "`" + game_type + "`" + newLinestring + gameMode_string + "`" + game_mode + "`" + newLinestring + newLinestring + lastLogin_string + "`" + str(log_in_converted) + "`" + newLinestring + lastLogout_string + "`" + str(log_out_converted) + "`" + newLinestring + newLinestring + "Last Game Ended: " + "`" + str(last_game_ended_converted) + "`"
