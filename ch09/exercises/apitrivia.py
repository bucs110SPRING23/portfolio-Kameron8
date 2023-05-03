import random
import requests

class TriviaProxyAPI:
    
    def __init__(self):
        self.url = "https://opentdb.com/api.php?"
        self.varstr = "amount=2&category=18"

    def get(self):
        url = self.url + self.varstr
        response = requests.get(url)
        data = response.json()
        return data ["results"]
    
    def main():
        tp = TriviaProxyAPI
        results = tp.get()
        response = requests.get("https://opentdb.com/api.php?amount=10&category=18") #amount is # of questions and category is the categor in this case 18 is computer science
        data = response.json() #Provides us with all the data we need 
        results = data["results"]

        for r in results: 
            print(r["question"])
            possibles = [r["correct_answer"]], [*r["incorrect_answers"]] #Star in front of the r makes the list spread out
            random.shuffle(possibles)
            print("Make your selection: ")
            for i, p in enumerate(possibles):
                print(f"{i}) {p}")
        
            selection = int(input(": "))
            if possibles[selection] == ["correct answer"]:
                print("You are correct")
            else: 
                print("You need to study harder! The correct answer is : {r['correct_answer']}")

