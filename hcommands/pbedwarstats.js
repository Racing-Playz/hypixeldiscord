import requests # We also import the maths library because it provides some functions we need
import math
from datetime import datetime, timezone, timedelta
import time

from hmisc import API_KEY

APIKEY = API_KEY.return_api_key()

def get_bedwars_stats(name):
    url = f"https://api.hypixel.net/player?key={APIKEY}&name={name}"
    res = requests.get(url)
    data = res.json()
    if data["player"] is None:
        return None

    bws_level = int(data["player"]["achievements"]["bedwars_level"])
    bws_wins = int(data["player"]["achievements"]["bedwars_wins"])
    bws_beds = int(data["player"]["achievements"]["bedwars_beds"])
    bws_kills = int(data["player"]["achievements"]["bedwars_bedwars_killer"])
    bws_games_played = int(data["player"]["stats"]["Bedwars"]["games_played_bedwars"])
    bws_final_kills = int(data["player"]["stats"]["Bedwars"]["final_kills_bedwars"])

    return "Level: " + "`" + str(bws_level) + "`" + "\n" + "Wins: " + "`" + str(bws_wins) + "`" + "\n" + "Beds Broken: " + "`" + str(bws_beds) + "`" + "\n" + "Kills: " + "`" + str(bws_kills) + "`" + "\n" + "Games Played: " + "`" + str(bws_games_played) + "`" + "\n" + "Final Kills: " + "`" + str(bws_final_kills) + "`" + "\n"
