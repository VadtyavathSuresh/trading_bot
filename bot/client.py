import os
from dotenv import load_dotenv
from binance.client import Client

def get_client():
    load_dotenv()
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    return client
