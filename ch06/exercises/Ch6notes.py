## Currently everything we do with our program is deleted from memory once the program is finished executions 
## How do we make a program remember across different executions --> Files 
## Files are essentially just saved program states 

#def main(): 
   # idea = input("Enter an Idea: ") #Need to get input from file 
  #  ideas = [] #Won't be saved across multiple iterations 
  #  ideas.append(idea)
 #   print(ideas) #Need to make it print to a file instead 


#Operating systems can manage files but programs cannot look at files 
# In order to read files we need to request the file from the operating system 
# Give operating system information --> Location of file, name of file, and how we are going to use the file 

# We can either read a file or writing the file, requires two different actions and modes 

import json

def read():
    file_pointer = open("assets/ideas.txt", "r") #Name is relative to whatever the main() function is being run from, r stands for read
    ideas = file_pointer.read() #Reads entire file, file needs to be saved  
    print(ideas) 
    # idea = file_pointer.readline() #Reads the document one line at a time, but the program will remember how far down in the file you are 
   # print(idea)
   # file_pointer.close() #resets the file and allows us to go back to the top of the document 
   # file_pointer is its own data type 

def write(): 
    file_pointer = open("assets/ideas2.txt", "w") #Writing to a file instead of reading it, if file exists it gets truncated, if it doesn't exist it will create a new file
    idea = input("Enter an idea: ")
    ideas = []
    ideas.append(idea)

    for i in ideas:
        file_pointer.write(i)  #Won't keep adding since open in write mode will clear the document every time  
    file_pointer.close()

def appendmode(): 
    file_pointer = open("assets/ideas2.txt", "a")
    idea = input("Enter an idea: ")
    ideas = []
    ideas.append(idea)

    for i in ideas:
        file_pointer.write(i + "\n") #\n is the symbol for the enter key, puts each input on a new line  
    file_pointer.close() #Always make sure to close files when writing to a file 


def main():
    read()
    appendmode()

main()


#Import json (at top of document) 
## json is a string format not a file format 

[
    1,
    "Hello",
    ["a","b","c"]
] #Creates a list in python

file_contents = open("assets/ideas.txt", "r").read()
print(file_contents) #makes everything a string 
data = json.loads(file_contents) #json converts everything to a list and the type it needs to be, standard for transferring data between programs 
