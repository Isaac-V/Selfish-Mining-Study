import http.client
import json

url = 'api.biteasy.com'
connection = http.client.HTTPSConnection(url, 443)
connection.request('GET', '/v2/btc/mainnet/blocks?type=ORPHANED&per_page=20')
response = connection.getresponse()
source = response.read().decode('utf-8')
data = json.loads(source)
print(data)