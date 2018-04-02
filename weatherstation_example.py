import requests
import json
OWM_KEY = '8ddb637e661cc63a87f16ca168924ad6'


class WeatherStation():
    def __init__(self):
        self.url = 'https://api.openweathermap.org/data/2.5/weather'
        self.auth_key = key

    def connect(self, **kwargs):
        package = {
            "APPID": self.auth_key,
            "units": "imperial"
        }
        package.update(kwargs)
        print(package)
        return requests.post('https://api.openweathermap.org/data/2.5/weather', params=package)


    def get_city_temp(self):
        q = input('What city would you like to check?: ')
        response = self.connect(q=q)
        return 'The weather in {} is {}.'.format(q.title(),response.json()['main']['temp'])

    def get_coords_temp(self):
        #lat={lat}&lon={lon}
        lat = input("What is the lat?: ")
        lon = input("What is the lon?: ")
        response = self.connect(lat=lat, lon=lon)
        print(response.url)
        print(response.json())
        return 'The weather in {} is {}.'.format(response.json()['name'],response.json()['main']['temp'])



if __name__ == '__main__':
    station = WeatherStation(OWM_KEY)
    print(station.get_city_temp())
