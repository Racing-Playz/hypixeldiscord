import requests # We also import the maths library because it provides some functions we need
import math
from datetime import datetime, timezone, timedelta
import time

from hmisc import API_KEY

APIKEY = API_KEY.return_api_key()

def get_friend_count(name):
    getUUID = f"https://api.mojang.com/users/profiles/minecraft/{name}"

    res = requests.get(getUUID)
    data = res.json()

    if data["id"] is None:
        return None

    returnUuid = (data["id"])

    url1 = f"https://api.hypixel.net/friends?key={APIKEY}&uuid=" + returnUuid

    res2 = requests.get(url1)
    data2 = res2.json()

    if data2["records"] is None:
        return None

    friend_count = len(data2["records"])

    return "Friends: " + "`" + str(friend_count) + "`"