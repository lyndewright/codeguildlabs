# Tell me the weather in my location by zip or city name.
# Ask me if I want the current temperature in Celsius or Fahrenheit and then display it.

import requests
import pytemperature

package = {
    'APPID': '8ddb637e661cc63a87f16ca168924ad6',
    'q': 'portland',
    'zip': '97202'
    }

print('*************Weather Station**************')


city_or_zip = input("Would you like to search by city or zip code?:" ).lower()
if city_or_zip == 'city':
    package['q'] = input("City Name: ").capitalize()
elif city_or_zip == 'zip code':
    package['zip'] = input("Zip: ")

r = requests.post('https://api.openweathermap.org/data/2.5/weather', params=package)

kelvin = r.json()['main']['temp']
f = pytemperature.k2f(kelvin)
c = pytemperature.k2c(kelvin)

temp = input("Would you like the temperature in Fahrenheit or Celsius [F/C]?: ").upper()
if temp == 'F':
    print('{} Fahrenheit.'.format(f))
elif temp == 'C':
    print('{} Celsius.'.format(c))
else:
    print("I didn't understand.")
