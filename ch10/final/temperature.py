import requests

class TemperatureAPI():

    def __init__(self, lat=51.507, lng=-0.1276):
        self.url1 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&daily=temperature_2m_max&temperature_unit=fahrenheit&forecast_days=1&timezone=auto"
        self.url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&daily=temperature_2m_min&temperature_unit=fahrenheit&forecast_days=1&timezone=auto"

    def getmax(self):
        weather = requests.get(self.url1)
        weatherdata = weather.json()
        weathercurrent = weatherdata ["daily"]
        bracketed_max = weathercurrent ["temperature_2m_max"]
        return str(bracketed_max)[1:-1]
    
    def getmin(self):
        weather = requests.get(self.url2)
        weatherdata = weather.json()
        weathercurrent = weatherdata ["daily"]
        bracketed_min = weathercurrent ["temperature_2m_min"]
        return str(bracketed_min)[1:-1]