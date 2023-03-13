def multiply(a,b):
    """
    This function takes two parameters and multiplies them together 
    args: 2 integers
    return: 1 integer
    """
    count = 1
    c = 0
    while b >= count:
        c = c + a
        count += 1
    return c

def exponent(a,b): 
    """
    This function takes two parameters and performs an exponent operation
    args: 2 integers
    return: 1 integer
    """
    count = 1
    c = 1
    while b >= count:
        c = c * a
        count += 1
    return c 

def square(a):
    """
    This function squares the input 
    args: integer 
    return: integer 
    """
    return exponent(a,2)

def main():
    print(multiply(5,10))
    print(exponent(3,3))
    print(square(4))

main()


