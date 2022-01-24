'''

Enunciado: Utilizando la API de https://openweathermap.org/ y realizando una petición a
https://api.openweathermap.org/data/2.5/weather?q={city%20name}&appid={apikey} , obtén la temperatura máxima y mínima,
para la ciudad que proporcione el usuario.

Objetivo:


    Aprender a utilizar librerías externas (en este caso, requests)

    Manipular el resultado de la petición (JSON)


'''

import requests

# r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Puente Genil&appid=AQUI LA API KEY')

# r.status_code

api_Key = 'PON AQUI LA API KEY'
web = 'https://api.openweathermap.org/data/2.5/weather?'

cityUser = str(input("Escribe la ciudad que quieras saber el tiempo: "))


# structure petition - web + "q=" + cityUser + "&appid=" + api_key. EXTENSION: If you need select temp. use
# &units=imperial for Fahrenheit, &units=metric for Celsius, nothing if you use Kelvin.

def getTemperature(cityUser, tempUser):
    petitionWeb = web + "q=" + cityUser + tempUser + "&appid=" + api_Key

    response = requests.get(petitionWeb)

    r = response.json()
    '''code 404 not gut'''

    if r["cod"] != "404":
        city = r["name"]
        temp_min = r["main"]["temp_min"]
        temp_max = r["main"]["temp_max"]

        # FUCK. read more API. default in Kelvin not Farenheit
        print(f"Ciudad Seleccionada:  {city} \n Temperatura mínima en grados = "
              f"{(round(temp_min, 2))}{tempScale}\n Temperatura máxima en grados = "
              f"{(round(temp_max, 2))}{tempScale}")


try:
    tempUser = int(input("Selecciona en que escala de temperatura deseas ver el tiempo: "))
    if tempUser == 1:
        tempUser = "&units=imperial"
        tempScale = "ºF"
        getTemperature(cityUser, tempUser)
    elif tempUser == 2:
        tempUser = "&units=metric"
        tempScale = "ºC"
        getTemperature(cityUser, tempUser)
    elif tempUser == 3:
        tempUser = ""
        tempScale = "K"
        getTemperature(cityUser, tempUser)
except ValueError:
    print("Error en la selección, por favor vuelva a intentarlo")

# print(r)

# {'coord': {'lon': -4.7574, 'lat': 37.406}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}],
# 'base': 'stations', 'main': {'temp': 288.2, 'feels_like': 287.25, 'temp_min': 288.2, 'temp_max': 288.2, 'pressure': 1024, 'humidity': 57,
# 'sea_level': 1024, 'grnd_level': 995}, 'visibility': 10000, 'wind': {'speed': 1.93, 'deg': 150, 'gust': 4.92}, 'clouds': {'all': 46},
# 'dt': 1642870714, 'sys': {'type': 1, 'id': 6394, 'country': 'ES', 'sunrise': 1642836558, 'sunset': 1642872690}, 'timezone': 3600, 'id': 6357251,
# 'name': 'Puente Genil', 'cod': 200}
