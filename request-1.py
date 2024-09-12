import requests

r=requests.get('https://api.gemini.com/v2/ticker/btcusd')

print(r)
price=r.json()
print(price['high'])
