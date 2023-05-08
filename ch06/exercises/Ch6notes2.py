# Protocols- 
# http 
# xml 
# json -current standard for saving structured data (saving a dictionary for example)
## All of them are STRING formats, NOT file formats 
## json only allows int, float, string, list, dicitonary, bools, and None

## {} is a dictionary 
## [] is a list 

#data = {
  #  "num": 1,
   # "msg": "Hello World",
#}

#json_string = json.dumps(data) #Turns entire thing into a string that could then be saved into a file, dumps data into a string  
#json_data = json.loads(json_string) 

#for k, v in json_data.items(): #k standing for key, and v standing for value
  #  print(k,v)

#fptr = open("assets/data.json", "w") #Creating a new file for teh data to be saved to 
#fptr.write(json_string)
#fptr.close()

 
#Way of loading data (?)
#fptr = json.load(open("assets/data.json", "r"))
#data = json.dump(data, fptr)
#fptr.close()
#print(data) #Data is now being displayed as a dictionary



# In order to add something to a json file and keep it acting as a json file you have to do 

import json

idea = input("Enter an idea: ")
file_pointer = open("assets/ideas.txt", "r")
data = json.load(file_pointer) #File needs to have something in it, for our case either [] or {}
data.append(idea)
file_pointer.close()
file_pointer = open("assets/ideas.txt", "w") 
json.dump(data, file_pointer) #Continues to add each new idea to the file 
file_pointer.close()

#If you want to programs to interact you have to create an intermediary file, where one program can load into it and then another can read from it
