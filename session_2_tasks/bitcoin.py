import requests

bitcoinurl=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(bitcoinurl.json()['bpi']['usd'])

