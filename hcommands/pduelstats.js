import requests # We also import the maths library because it provides some functions we need
import math
from datetime import datetime, timezone, timedelta
import time

from hmisc import API_KEY

APIKEY = API_KEY.return_api_key()

def get_duels_stats(name):
    url = f"https://api.hypixel.net/player?key={APIKEY}&name={name}"
    res = requests.get(url)
    data = res.json()
    if data["player"] is None:
        return None

    duels_wins = (data["player"]["achievements"]["duels_duels_winner"])
    duels_highest_ws = (data["player"]["achievements"]["duels_duels_win_streak"])
    duels_played = (data["player"]["stats"]["Duels"]["games_played_duels"])
    return "Wins: " + "`" + str(duels_wins) + "`" + "\n" + "Best Winstreak: " + "`" + str(duels_highest_ws) + "`" + "\n" + "Games Played: " + "`" + str(duels_played) + "`"
