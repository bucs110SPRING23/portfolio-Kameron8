import requests

class AdviceSlipAPI:
    
    def __init__(self):
        """
        intializes the AdviceSlipAPI in order to generate advice/fortunes for the user 
        args: self 
        rerturn: none
        """
        self.url = "https://api.adviceslip.com/advice"

    def get(self):
        """
        extracts the information from the API, in this case it isolates only the advice 
        args: self 
        return: random_advice (str)
        """
        advice = requests.get(self.url)
        advicedata = advice.json()
        random_advice = advicedata ["slip"]
        return random_advice["advice"]


