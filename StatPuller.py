import urllib.parse
import urllib.request
import json

url = 'https://api.biteasy.com/v2/btc/testnet/blocks?type=ORPHANED&per_page=20'
response = json.load(urllib.request.urlopen(url))
print(response)