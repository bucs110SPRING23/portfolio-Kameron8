def main():
        asapi = AdviceSlipAPI
        results = asapi.get()

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