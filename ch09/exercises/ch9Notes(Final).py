# Requests and API 

# Data you need is usually not on yuor computer but it is rather somewhere else 

# Network programming 
## Build a program that asks trvia questions 

## Server - Any computer "listening" for incoming network connections. Technically your phone is a server and pretty much every computer 

## Requests: Incoming connections that asks for some resource for the server (images, video, music, text, json, html)

## Different types of requests: 
### GET - "Read" operation (anyone can usually receive information)
#### Visiting, downloading a file, etc. 
### PUT - "Write" operation (requires security; not anyone can edit a resouce)
#### Login, deleting a file, 


# Headers - Sent with request and the response 
## Status codes
### 200: Ok, everything went fine 
### 400: Resource cannot be delivered 
### 404: Not found
### 500: Bad code on the server 
## ip address
## system information (geolocation)


#urllib (doesnt work super well)

# Instead we will use python request library 



import requests #Need to do pip install

def example(): 
    response = requests.get("http://icanhazip.com") #Sends your ip address back to you 
    print(response.staus_code) #Whether or not the request went through (200 means everything is good)
    print(response.headers) #Sends back all headers
    print(response.text)



# Use API (Application Programmer's Interface)n
## API's can return data in any format, but usually returned in json 

## locate free API's (linked on CS110 Website)
### Focus on the ones that do not require any authorization 

# Need to understand how url parameters work in order to use API's 

## "?" #Anything after a question mark is a variable that you can edit 
## "&" #Used to sepearate out the different variables within a url 

##binghamton.edu/cs # Mainpage is binghamton.edu and we go into the sub "folder" cs 

## open trivia database (opentdb.com)

import random

def example2():
    response = requests.get("https://opentdb.com/api.php?amount=10&category=18") #amount is # of questions and category is the categor in this case 18 is computer science
    data = response.json() #Provides us with all the data we need 
    results = data["results"]

    for r in results: 
        print(r["question"])
        possibles = [r["correct_answer"]], [*r["incorrect_answers"]] #Star in front of the r makes the list spread out
        random.shuffle(possibles)
        print("Make your selection: ")
        for i, p in enumerate(possibles):
            print(f"{i}) {p}")
        
        selection = int(input(": "))
        if possibles[selection] == ["correct answer"]:
            print("You are correct")
        else: 
            print("You need to study harder! The correct answer is : {r['correct_answer']}")