import requests
import datetime

api_url="https://easycrypto.co.za/api/Currency/GetDCXTotalBalance"
requests.packages.urllib3.disable_warnings()
response = requests.get(api_url, verify=False)
data = response.json()

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S")+ " EC10 price R%0.2f"%(data["TokenZarPrice"]))
