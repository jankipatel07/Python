#from urllib.request import Request, urlopen
import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'

#parameters = {'upc': '012993441012'}
parameters = {'upc': '073366118238'}

#req = Request(baseUrl, headers={'user-Agent': 'Chrome/84.0'})
#response = urlopen(req).read()

response = requests.get(baseUrl, params=parameters)
print (response.url)

jsonContent = response.content
jsonInfo = json.loads(jsonContent)
item = jsonInfo['items'][0] 
print (item['title'])
print (item['brand'])
