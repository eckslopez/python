import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
#print(json['people'][1]['name'])
for person in json['people']:
    print(person['name'])
for person in json['people']:
    print(person['craft'])