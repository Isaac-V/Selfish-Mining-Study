import http.client
import json

url = 'blockchain.info'
connection = http.client.HTTPSConnection(url, 443)
connection.request('GET', '/blocks/BTCC Pool?format=json')
response = connection.getresponse()
source = response.read()
#print(source)
decoded = source.decode('utf-8')
data = json.loads(decoded)
bTotal = len(data['blocks'])

for bIndex in range(bTotal):
    print(data['blocks'][bIndex]['height'])
    
print(bTotal)
