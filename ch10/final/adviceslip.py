import requests

class AdviceSlipAPI:
    
    def __init__(self):
        self.url = "https://api.adviceslip.com/advice"

    def get(self):
        advice = requests.get(self.url)
        advicedata = advice.json()
        random_advice = advicedata ["slip"]
        return random_advice["advice"]


