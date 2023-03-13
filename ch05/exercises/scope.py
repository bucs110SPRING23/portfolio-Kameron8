def multiply(a,b):
    count = 1
    c = 0
    while b >= count:
        c = c + a
        count += 1
    return c

def exponent(a,b): 
    count = 1
    c = 1
    while b >= count:
        c = c * a
        count += 1
    return c 

def square(a):
    return exponent(a,2)

def main():
    print(multiply(5,10))
    print(exponent(3,3))
    print(square(4))

main()


