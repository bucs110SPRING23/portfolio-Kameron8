from adviceslip import AdviceSlipAPI
from sunset import SunsetAPI
from temperature import TemperatureAPI
import requests

def main():
    for _ in range(5):
        print('\n')
    print("Welcome to your weather report. Please enter your longitude and latitude to find out the temperature, the sunset time, and to recieve some advice for the day!")
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
    print(f"The sun will be setting at {sunset_time} UTC tonight. The high and low for today is {maxtemperature} and {mintemperature} degrees Fahrenheit. Finally, your advice for the day is '{advice_slip}' Enjoy the rest of your day!")

main()