import requests

r = requests.get('http://api.icndb.com/jokes/random')

#print(r.json())

response = r.json()

strng = 'Joke ID: {}\nJoke: {}'.format(response['value']['id'], response['value']['joke'])

print(strng)
