from json import load
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]
BOT_USERNAME = os.environ["BOT_USERNAME"]
BOT_URL = os.environ["BOT_URL"]

WELCOME_MESSAGE = """
Welcome to CheepFuel bot, this bot provides the service to fetch the best prices for fuel,
Please enter one of the regional options below to fetch the prices.

1. All
2. VIC
3. NSW
4. QLD
5. WA
"""
REGIONS = ["ALL", "VIC", "NSW", "QLD", "WA"]

API_URL = "https://projectzerothree.info/api.php?format=json"
