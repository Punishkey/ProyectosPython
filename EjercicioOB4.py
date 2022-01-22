'''

Enunciado: Utilizando la API de https://openweathermap.org/ y realizando una petición a
https://api.openweathermap.org/data/2.5/weather?q={city%20name}&appid={apikey} , obtén la temperatura máxima y mínima,
para la ciudad que proporcione el usuario.

Objetivo:


    Aprender a utilizar librerías externas (en este caso, requests)

    Manipular el resultado de la petición (JSON)


'''

import requests

# r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Puente Genil&appid=PON AQUI LA API KEY')

# r.status_code

api_Key = 'PON AQUI LA API KEY'

cityUser = str(input("Escribe la ciudad que quieras saber el tiempo: "))

web = 'https://api.openweathermap.org/data/2.5/weather?'

# structure petition - web + "q=" + cityUser + "&appid=" + api_key

petitionWeb = web + "q=" + cityUser + "&appid=" + api_Key

response = requests.get(petitionWeb)

r = response.json()

'''code 404 not gut'''

if r["cod"] != "404":
    city = r["name"]
    temp_min = r["main"]["temp_min"]
    temp_max = r["main"]["temp_max"]

    print("Ciudad Seleccionada: " + city +
          "\n Temperatura mínima en grados = " +
          str((temp_min - 32) / 18) +
          "\n Temperatura máxima en grados = " +
          str((temp_max - 32) / 18))

# print(r)

# {'coord': {'lon': -4.7574, 'lat': 37.406}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}],
# 'base': 'stations', 'main': {'temp': 288.2, 'feels_like': 287.25, 'temp_min': 288.2, 'temp_max': 288.2, 'pressure': 1024, 'humidity': 57,
# 'sea_level': 1024, 'grnd_level': 995}, 'visibility': 10000, 'wind': {'speed': 1.93, 'deg': 150, 'gust': 4.92}, 'clouds': {'all': 46},
# 'dt': 1642870714, 'sys': {'type': 1, 'id': 6394, 'country': 'ES', 'sunrise': 1642836558, 'sunset': 1642872690}, 'timezone': 3600, 'id': 6357251,
# 'name': 'Puente Genil', 'cod': 200}
