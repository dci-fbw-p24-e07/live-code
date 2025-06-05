import requests

url = 'https://digitalcareerinstitute.org/'
r = requests.get(url)
print(f"Status code for {url} is {r.status_code}")