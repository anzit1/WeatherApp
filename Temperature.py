class Temperature:
    def __init__(self,city,temperature,humidity,wind):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.wind = wind

    def info(self):
        print(f"CITY -> {self.city} | TEMPERATURE -> {self.temperature} | HUMIDITY -> {self.humidity} | WIND -> {self.wind}")