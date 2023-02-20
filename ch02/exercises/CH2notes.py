# bool - boolean value #Type of data realting to logic
# True/False 
# - Caps are important
# Boolean means anything that results in a single true or false

print(type(True))

# Almost anything can be cast as a bool in python

print(bool(1))
print(bool(-1))
print(bool("Hello")) #All of the previous print commands are all true 
print(bool(0))
print(bool(""))
print(bool([])) #All three of the previous are false, usually empty container data 

#Boolean expressions 

x = 5 
y = 10

#Boolean operators 

print(x==y) #Check for equality (have to use two equal signs) (false)
print(x>y) #False
print(x<y) #True
print(x>=y) #False #Greater than or equal to symbol has to go before the equals sign in both situations
print(x<=y) #True
print(x != y) #Not equal to each other

#Semantic operators (and, or, not)

#and: and == True when x and y are both true 

print(True and True) #Outputs true
print(True and False) #False
print (False and False) #False

#or - At least one has to be true (both still can be)
print(True or True) #True
print(True or False) #True
print(False or False) #False

#not - negation neither can be true 
print(not True) #Outputs false
print(not False) #Outputs true 

print("apple" == "apple")
print("apple" < "Apple Pie") 
print(ord("a"), ord("A")) #a is 97 while A is 65 so technically lowercase a is a greater value and apple is greater than apple pie 

# Is 
print(1 is int) #Is 1 an integer? (False)
print(1 is 1) #True 

print(1 is 5/5) #False: 5 is a float while 1 is an integer 
print(1 == 1.0) #True
print(1 is 5//5) #Returns an int so this one is true 


mynums = [1,2,3,4,5,6,7]
print(1 in mynums) #Is 1 in the list mynums? True
print(10 in mynums) #Is 10 in the list mynums? False
print(1.0 in mynums) #Outputs true 
print(5-2 in mynums) #Outputs true
print(2-5 in mynums) #Outputs false 

#Check if a is a negative value and if it is get the absolute value of it 
#Conditional execution (if statement)

a = 200 

if a < 0: #Requires a colon at the end 
    a = abs(a) #indentation 
else: #No condition, still have a colon, when the if statement is false then the else code will run 
    print("positive")

print(a) #Deident anything that should not be part of the if statement 

x = 12

if x > 5:
    if x > 10:
        print("x is greater than 10")
    else: 
        print("x is greater than 5")
else: 
    print("x is less than or equal to 5")


#Will print whether x is greater than 5, greater than 10, or less than 5 and only have one output

#elif- always goes between the if and else 

#y = int(input("Enter a Number:"))

#if y > 10:
        #print("y is greater than 10")
#elif y > 5: 
        #print("y is greater than 5")
#else: 
    #print("y is less than or equal to 5")

#Most selective condition has to go first when using elif statements 

#if <boolean condition>: required 
    # Does something
# elif <Boolean condition>: optional 
    # Do something 
#else: #optional 
    #Do something if no other conditions were met 

#Fizz Buzz- Loop through a range of values provided by the user
# For each value in the range if the value is divisible by 3, print "fizz"
# If divisible by 5, print "buzz" 
# if divisible by both 3 and 5 print "fizzbuzz"

z = int(input("Enter an Upper Limit:"))
for i in range(z+1): #Actually outputs the upper limit that the user inputs 
    print("number: ", i)
    if i % 3 == 0 and i % 5 == 0: 
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print("no")

