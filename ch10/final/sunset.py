import requests

class SunsetAPI():

    def __init__(self, lat=51.507, lng=0.1276):
        """
        intializes the SunsetAPI in order to generate sunset time for the user.
        args: self 
        rerturn: none
        """
        self.url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date=today"

    def get(self):
        """
        extracts the information needed from the url
        args: self 
        return: sunsettime(str)
        """
        times = requests.get(self.url)
        timedata = times.json()
        sunsettime = timedata ["results"]
        return sunsettime ["sunset"]
