import requests

url = 'https://api.weatherapi.com/v1/current.json?key=b6197392005b4759ba022357232509&q=91752&aqi=no'
response = requests.get(url)
weatherapi_json = response.json()

print("The current temperature in " + weatherapi_json['location']['name'] + " is: " + str(weatherapi_json['current']['temp_f']) + " degrees Fahrenheit.")
