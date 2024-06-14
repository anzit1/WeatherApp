import kivy
from Temperature import Temperature
import datetime as dt
import requests

kivy.require('1.9.0')


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = "Alicante"


def convertKel_to_Cel(tempKelvin):
    celsius = tempKelvin - 273.15
    return celsius


url = BASE_URL + "appid=" + "adff6968135cda54be6b312349166a0e" + "&q=" + CITY
response = requests.get(url).json()

longi = response['coord']['lon']
lati = response['coord']['lat']
print(f"Longitud -> {longi}º || Latitud -> {lati}º")
temp_kelvin = response['main']['temp']
temp_celsius = convertKel_to_Cel(temp_kelvin)
print(response)