import requests
import datetime
from pycoingecko import CoinGeckoAPI
import json

ec_api_url="https://api.easycrypto.co.za/api/v2/GetPrice"
requests.packages.urllib3.disable_warnings()
response = requests.get(ec_api_url, verify=False)
data = response.json()

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

for i in data:
    if i['Symbol'] == 'EC10' or i['Symbol'] == 'ECE10' or i['Symbol'] == 'ECA20':
        print("%s R%0.2f" % (i['Symbol'], i['Zar']['BidPrice']))

cg = CoinGeckoAPI()
coin_prices = cg.get_price(ids='bitcoin,ethereum,cardano,binance,solana,terra-luna', vs_currencies='usd')


for coin, price in coin_prices.items():
    print('%s \t $%s' % (coin.capitalize(), price['usd']))
