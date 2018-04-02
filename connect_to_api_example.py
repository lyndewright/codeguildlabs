import requests

packaage = {
    'APPID': '8ddb637e661cc63a87f16ca168924ad6',#your API key
     'q': 'portland'
}

r = requests.post('https://api.openwaethermap.org/data/s.5/weather', params=package)#?q={city name}')

print(r.txt)


#my unique API/Key ID: 8ddb637e661cc63a87f16ca168924ad6
