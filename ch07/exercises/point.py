import random
import pygame

class LED:  
    
    def __init__(self, x=0,y=0,color="red"): #self is the instance being created 
        self.xcoor = abs(x) #dot operator accessess instance variables of object 
        self.ycoor = abs(y)
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), 5, 5)
        self.color = color
        self.radius = 10

    def random_color(self):
        colors = ["blue", "purple", "orange", "pink"]
        self.color = random.choice(colors)


## Function does not return 


# User types/classes always start with a capital letter 
# Usually, classes go in their own file 
# One class per file 
# Anything with double underscores on both sides is a dunder 

#Functions are called methods when they are in a class 
#All methods have their first paramter as "self"