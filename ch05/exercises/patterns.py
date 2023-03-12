def prompt():
     print("Please Enter A Number: ")
     
def star_pyramid():
    for i in range(1,a+1):
            print(i*"* ", end= " ")
            print("\n")

def rstar_pyramid():
    for i in reversed(range(1,g+1)):
         print(i*"* ", end= " ")
         print("\n")


prompt()
a = int(input(": "))
star_pyramid()
prompt()
g = int(input(": "))
rstar_pyramid()