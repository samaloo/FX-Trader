import requests
import defs

session = requests.Session()

instrument = "EUR_USD"
count = 10
granularity = "H1"

url = f"{defs.OANDA_URL}/instruments/{instrument}/candles" 