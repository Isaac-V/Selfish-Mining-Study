import http.client
import json

url = 'api.biteasy.com'
connection = http.client.HTTPSConnection(url, 443)
connection.request('GET', '/v2/btc/mainnet/blocks?page=1&per_page=200')
response = connection.getresponse()
source = response.read().decode('utf-8')
data = json.loads(source)
print(data['data']['pagination'])
print(data['data']['blocks'][0])
bTotal = len(data['data']['blocks'])

for bIndex in range(bTotal):
    print(data['data']['blocks'][bIndex]['solved_at'])
    
print(bTotal)
