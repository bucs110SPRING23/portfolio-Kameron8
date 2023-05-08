import random 

winningnumber = random.randrange(1, 11)

for _ in range(3):
    message = """
        Guess a number between 1 and 10 
        """

    response = int(input(message))

    if response > winningnumber:
        print("Too High!")
    elif response < winningnumber:
        print("Too Low!")
    elif response == winningnumber:
        print("Correct!")
        break