import requests

r = requests.get('http://api.icndb.com/jokes/random')

print(r.json())
