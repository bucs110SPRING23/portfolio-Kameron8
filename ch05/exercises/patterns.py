def prompt():
     print("Please Enter A Number: ")
     a = int(input(": "))
     return a 

     
def star_pyramid(a):
    for i in range(1,a+1):
            print(i*"* ", end= " ")
            print("\n")

def rstar_pyramid(a):
    for i in reversed(range(1,a+1)):
         print(i*"* ", end= " ")
         print("\n")

def main():
     star_pyramid(prompt())
     rstar_pyramid(prompt())

main()