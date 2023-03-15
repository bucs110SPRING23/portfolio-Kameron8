def multiply(a,b):
    """
    This function takes two parameters and multiplies them together 
    args: a (int), b (int)
    return: (int)
    """
    count = 1
    c = 0 #Accumulator
    while b >= count:
        c = c + a
        count += 1
    return c

def exponent(a,b): 
    """
    This function takes two parameters and performs an exponent operation
    args: a (int), b (int)
    return: (int)
    """
    count = 1
    c = 1 #Accumulator does not always need to start at zero 
    while b >= count:
        c = c * a
        count += 1
    return c 

def square(a):
    """
    This function squares the input 
    args: a (int) 
    return: (int) 
    """
    return exponent(a,2)

def main():
    a = int(input("Enter a Number: "))
    b = int(input("Enter a Number: "))
    print(multiply(a,b))
    print(exponent(a,b))
    print(square(a))

main()


