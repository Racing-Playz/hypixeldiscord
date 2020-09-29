import requests # We also import the maths library because it provides some functions we need
import math
from datetime import datetime, timezone, timedelta
import time

import random

#one api key should be enough, but if you get api exceeded errors add another one (by going on an alt and typing /api in the chat).

def return_api_key():
    API_KEY = ["Y8bb07638-1de4-46e7-8133-af9bfb0e67f9"]
    return random.choice(API_KEY)
    #This just chooses a random api key
    #for each request to prevent throttling
    #it wont affect anything if there is only one api key in the list
