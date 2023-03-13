def prompt():
     """
     This is a function that displays the prompt and returns the value needed to draw the pyramids 
     args: none
     return: integer
     """
     print("Please Enter A Number: ")
     a = int(input(": "))
     return a 
   
def star_pyramid(a):
    """
    This is a function that creates a star pyramid smallest to biggest
    args: integer
    return: string  
    """
    for i in range(1,a+1):
            print(i*"* ", end= " ")
            print("\n")

def rstar_pyramid(a):
    """
    This is a function that creates an inverted star pyramid smallest to biggest
    args: integer
    return: string  
    """
    for i in reversed(range(1,a+1)):
         print(i*"* ", end= " ")
         print("\n")

def main():
     star_pyramid(prompt())
     rstar_pyramid(prompt())

main()