from Temperature import Temperature
import datetime as dt
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
import requests

class Home(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initUI()


    def initUI(self):
#Define "propriedades" do UI
        self.title = Label(text="Lopeirada Weather App", font_size = '40sp', font_name="Arial")
        self.city_name = TextInput(readonly=True)
        self.temperature = Label(text="Temperature", font_size = '35sp', font_name="Arial")
        self.humidity = Label(text="Humidity", font_size='35sp', font_name="Arial")
        self.windspeed = Label(text="Wind Speed", font_size='35sp', font_name="Arial")
        self.temperature_value = Label(text="null", font_size='30sp', font_name="Arial")
        self.humidity_value = Label(text="null", font_size='30sp', font_name="Arial")
        self.windspeed_value = Label(text="null", font_size='30sp', font_name="Arial")
        self.input_city = TextInput(hint_text='Enter city name.', size_hint=(1,0.8))
        self.button_ok = Button(text="OK")

#Setup do Boxlayout com duas colunas
        self.master = BoxLayout()
        col1 = BoxLayout(orientation = 'vertical', padding = 10)
        col2 = BoxLayout(orientation = 'vertical', padding = 10)

#Coloca Widgets na primeira coluna
        col1.add_widget(self.title)
        col1.add_widget(self.city_name)
        col1.add_widget(self.temperature)
        col1.add_widget(self.humidity)
        col1.add_widget(self.windspeed)
        col1.add_widget(self.input_city)

# Coloca Widgets na segunda coluna
        col2.add_widget(self.temperature_value)
        col2.add_widget(self.humidity_value)
        col2.add_widget(self.windspeed_value)
        col2.add_widget(self.button_ok)

#Coloca colunas no master -> master colocado no screen
        self.master.add_widget(col1)
        self.master.add_widget(col2)
        self.add_widget(self.master)


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name="Home"))
        return sm
if __name__ in "__main__":
    MainApp().run()














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