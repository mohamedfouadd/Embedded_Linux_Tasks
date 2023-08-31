import requests
#import json

ip_url = requests.get('https://api.ipify.org/?format=json')
ip_data = ip_url.json() 
x = ip_data['ip'] 

location_url = requests.get(f'https://ipinfo.io/{x}/geo')
location_data = location_url.json()  

print(location_data)