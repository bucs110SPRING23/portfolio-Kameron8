## Iteration / Looping over objects data 
## Something is iterable if you can loop over it 

# mystr = "hello"
# mynums = [1,2,3,4,5]

# for ch in mystr:
   # print("yes")

# for num in mynums:
   # print("yes")

## Anything iterable can be 'indexed' into 

#print(mystr [1])

#mynums[0] = 5 #Works because it is mutable and can be changed after assignment 
#mystr[0] = "J" #Does not work because strings are not mutable after being set 

# mystr is immutable

#mynums = [1,2,3,4,5]
#myothernums = [1,2,3,4,5]

#if mynums == myothernums:
    #print("Yes!")
#if mynums is myothernums: #Only get the yes to be printed because numbers are mutable and therefore these are not the same exact data despite being of the same value 
    #print("No!")

#If we were dealing with two strings that were the same message then using 'is' would work since they are not mutable and therefore they are the exact same piece of information 

#Substring 

#mystr = "hello"
#print(mystr[0], mystr[1:4]) #Indexing starts at zero so one is the 2nd letter and the 4 is inclusive 

#mystr = "J" , mystr[1:5] #This is wrong but in theory it should print out "Jello"
#print(mystr)

# Iterable objects are not always mutable, you can perform functions do an immutable object but the information itself will not change 

# Slicing with mutable objects 

#mynums = [1,2,3,4,5]

#mynums[2:2] = [2.5] #Adds a 2.5 in between the two and the three, the 2.5 needs to be in brackets even if it is not a list, but can add more numbers and make it a list 
#print(mynums)


mynums = [1,2,3,4,5]

#for i in mynums:
   # i = i * 2
   # print(i) #Multiplies each value in mynums by two
#print(mynums) #Does not actually change the values of mynums itself, just operations were performed to them 

#for i, v in enumerate(mynums): #Allows you to change the actual values within mynums 
    #mynums[i] = v * 2 #i = index location in list, v = value at index location
#print(mynums)


## Lists can very slow and making them immutable allows programs and computers to run faster 

#Tuples 

#mynums = (4, 12, 68, 3) #Using parantheses instead of brackets!! Creates an immutable list known as a Tuple

#mynums[2] = 2.5 #Won't work because you can't assign anything to it 
#Use tuples wherever possible and it will reduce a lot of lag in a program 

#x = 3 
#y = 6

#temp = x
#x = y
#y = temp #Basic swap algorithm and works bevause of tuples 

#x, y = y, x #Swapping algorithm: don't need parantheses 

#num = [5] * 3
#print(num)

#num = (5,) * 3 #Single element tuples MUST have a trailing comma
#print(num)

#Tuples are lists you can't change once you create them 


#contacts = [
    #["Bill", "867-5309"],
   #["Jane", "555-1212"]
#]

#name = input("Enter a name: ")

#for contact in contacts:
    #if contact[0] == name:
        #print(contact[1])
       # break

##Above example not efficient as the list gets longer so we need a more efficient way 

##need to relate the index to a value 

##Can do this by using a strategy called a dictionary 

#contact = { #Use squiggly brackets in order to create a dictionary where each contact is indexable by name 
    #"Bill": "867-5309",
   # "Jane": "555-1212"
#}

#contact["Joe"] = "314-1592" #Add joe to the list of contacts, if Joe was already in the list it will update the current key 
## numbers can be the same as one another though 

#name = input("Enter a name: ")

#print(contact=name)

# list[index] = value 
# dictionary[key] = value 
# key/value pairs 
# keys must be unique and immutable; usually strings are used for the keys (names in our examples)

#for c in contact:
    #print(c) #Prints out just the key
   # print(contact[c]) #Prints out the key and the value 

#for key, value in contact.items: #Similar to enumerate 
   # print(key)
   # print(value) 


#Use get() only for reading and doesn't break the program if something is not present in the dictionary 

   # if contact.get("juan"):
        #print(contact["juan"])

#While loop can be used for infinite amount of iterations 

# i = 0 #Iterating variable 
# while i < 10: 
   # print(i)
   # i += 1 #Iterating variable must change in order for while loops to work properly

#Any for loop can be recreated with a while loop 
#Some while loops canNOT be recreated with for loops 