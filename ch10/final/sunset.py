import requests

class SunsetAPI():

    def __init__(self, lat=51.507, lng=0.1276):
        self.url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date=today"

    def get(self):
        times = requests.get(self.url)
        timedata = times.json()
        sunsettime = timedata ["results"]
        return sunsettime ["sunset"]
