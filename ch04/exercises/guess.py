import random 

winningnumber = random.randrange(1, 1001)
print(winningnumber)

message = """
    Guess a number between 1 and 1000
    """

response = int(input(message))

response = 0

while winningnumber != response:
    if response > winningnumber:
        print("Too High!")
    elif response < winningnumber:
        print("Too Low!")

    

print("Correct!")

