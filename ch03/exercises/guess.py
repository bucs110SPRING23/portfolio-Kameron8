import random 

winningnumber = random.randrange(11)

for _ in range(3):
    message = """
        Guess the number 
        """

    response = int(input(message))

    if response > winningnumber:
        print("Too High")
    elif response < winningnumber:
        print("Too Low")
    elif response == winningnumber:
        print("correct!")
        break