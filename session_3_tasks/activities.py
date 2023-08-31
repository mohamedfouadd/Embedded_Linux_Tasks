import time
import requests


url=requests.get('https://www.boredapi.com/api/activity')
time.sleep(2)
print(url.json()['activity'])
