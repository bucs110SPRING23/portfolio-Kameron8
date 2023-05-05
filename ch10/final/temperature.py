import requests

class TemperatureAPI():

    def __init__(self, lat=51.507, lng=-0.1276):
        """
        intializes the TemperatureAPI in order to allow for both the high and low temperature to be reported back to the user
        args: self 
        rerturn: none
        """
        self.url1 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&daily=temperature_2m_max&temperature_unit=fahrenheit&forecast_days=1&timezone=auto"
        self.url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&daily=temperature_2m_min&temperature_unit=fahrenheit&forecast_days=1&timezone=auto"

    def getmax(self):
        """
        returns the maximum temperature for a given day at a specific location
        args: self
        return: bracketed_max(str) the data which relays the maximum temperature
        """
        weather = requests.get(self.url1)
        weatherdata = weather.json()
        weathercurrent = weatherdata ["daily"]
        bracketed_max = weathercurrent ["temperature_2m_max"]
        return str(bracketed_max)[1:-1] #Removing the brackets from the information
    
    def getmin(self):
        """
        returns the minimum temperature for a given day at a specific location
        args: self
        return: bracketed_min(str) the data which relays the minimum temperature
        """
        weather = requests.get(self.url2)
        weatherdata = weather.json()
        weathercurrent = weatherdata ["daily"]
        bracketed_min = weathercurrent ["temperature_2m_min"]
        return str(bracketed_min)[1:-1] #Removing the brackets from the information