from adviceslip import AdviceSlipAPI
from sunset import SunsetAPI
from temperature import TemperatureAPI
import requests

class Controller: 

    def mainloop(self): 
        """
        starts by telling the user to input their longitude and latitude in order to get their weather report. stores that information and then uses it to generate the information for the user before printing it out
        args: self, lat (str), lng(str), neither lat or lng are not arguments to the function itself, but are generated as the program runs 
        return: (str) End result which displays all of the aforementioned information to the user
        """
        for _ in range(5):
            print('\n')
        print("Welcome to your weather report. Please enter your longitude and latitude to find out the temperature for today, the sunset time, and to recieve a fortune!")
        advice = AdviceSlipAPI()
        advice_slip = AdviceSlipAPI.get(advice)
        lat = str(input("Latitude: "))
        lng = str(input("Longitude: "))
        sunset = SunsetAPI(lat, lng)
        sunset_time = SunsetAPI.get(sunset)
        tempmax = TemperatureAPI(lat,lng)
        maxtemperature =  TemperatureAPI.getmax(tempmax)
        tempmin = TemperatureAPI(lat,lng)
        mintemperature =  TemperatureAPI.getmin(tempmin)
        print(f"The sun will be setting at {sunset_time} UTC tonight. The high and low for today is {maxtemperature} and {mintemperature} degrees Fahrenheit. Finally, your advice for the day is '{advice_slip}'")


