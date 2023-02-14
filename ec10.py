import requests
import datetime
from pycoingecko import CoinGeckoAPI

ec_api_url="https://api.easycrypto.co.za/api/v2/GetPrice"
requests.packages.urllib3.disable_warnings()

try:
    response = requests.get(ec_api_url, verify=False)
    data = response.json()

    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

    symbols = ['EC10', 'ECE10', 'ECA20', 'ECNMG']
    for crypto in [i for i in data if i['Symbol'] in symbols]:
        print("%s R%0.2f" % (crypto['Symbol'], crypto['Zar']['BidPrice']))
except requests.exceptions.ConnectionError as ce:
    print("Connection error calling  EasyCrypto url %s" % ec_api_url )

# Use CoinGecko api
cg = CoinGeckoAPI()
try:
    coin_prices = cg.get_price(ids='bitcoin,ethereum,cardano,binance,solana,terra-luna', vs_currencies='usd')

    for coin, price in coin_prices.items():
        print('%s \t $%s' % (coin.capitalize(), price['usd']))
except requests.exceptions.ConnectionError as ce:
    print("Connection error calling  CoinGecko url %s" % ce.request.url )
