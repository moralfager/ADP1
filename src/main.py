from pycoingecko import CoinGeckoAPI
import json, operator
cg = CoinGeckoAPI()
data1 = cg.get_coins_markets(vs_currency="usd")
path = "example.json"
with open("example.json", "w") as json_file:
    json.dump(data1, json_file, indent=2)
count = 0
data1.sort(key=operator.itemgetter('market_cap'), reverse=True)
for x in data1:
    print(str(data1[count]["id"])+" "+str(data1[count]["market_cap"]))
    count = count + 1
