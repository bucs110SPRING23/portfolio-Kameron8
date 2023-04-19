import random
import pygame

class LED:  
    
    def __init__(self, x=0,y=0, size = 20): #self is the instance being created 
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), size)
        self.color = self.random_color()

    def random_color(self):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            

## Function does not return 


# User types/classes always start with a capital letter 
# Usually, classes go in their own file 
# One class per file 
# Anything with double underscores on both sides is a dunder 

#Functions are called methods when they are in a class 
#All methods have their first paramter as "self"