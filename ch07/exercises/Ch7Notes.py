# Managing complexity - Advancing programming just manages complexity 
# Unix - 10000 SLOC (source lines of code)
# Chrome - 10,000,000 SLOC 
# OS X - 100,000,000 SLOC 

# Complex Objects 
# - primitives: int, str, float, lists, dict, tuple, etc. 
# - complex: Turtle- x, y, heading, color, pensize, shape 

# Bundle data and functions together 
# State: the current value(s) of the data in the object 
# Behaviour: the functions that operate on the data in the object 

# Point 
# - object should do one thing 
# state: x, y, color 
# behaviour: change_color, move

# Classes == Type (Type built out of other objects)

#import turtle 

#print(type(turtle.Turtle())) #Complex type
#print(type(1)) #Primitive type 

#Classes are essentially blueprints for an object 
# - functions are stored algorithms 
# - class is a stored data type 
# - classes are not executable 
# - don't put executable code in global scope, definitions are fine 

#Point class 
# - Instance: an object created from a specific class 
#     - t : turtle.Turtle() t is an instance of Turtle 
# - Instance variable: an internal variable that is a part of an instance 
#      - t.x, t.pos : x and pos are instance variables 
# - Interface: the functions and variables of an object 
#     -t.forward(): .forward() part of the interface of turtle 


# Point - Make it a class ourselves

#Make it in point.py 
#def make_point(x,y):
#class Point: 
    # User types/classes always start with a capital letter 
    # Usually, classes go in their own file 
    # One class per file 
    # Anything with double underscores on both sides is a dunder 
    #def __init__(self): #self is the instance being created 
       # self.x = 0 #dot operator accessess instance variables of object 
        #self.y = 0
        #self.color = ""


## In main.py we can import point in 
#import point 

#p1 = point.Point() #Go into point module and find Point class 
# p1 is an instance of point, point is a class
#p1.x= 10

#p2 = point.Point()
#p2.x = 5 

#State of p1 and p2 at this line 
## p1: x=10, y=0, empty string for color 
## p2: x=5, y=0, empty string for color 

#p1.color = "red"
# state of p1: x=10, y=0, color="red"

##Classes should be named with TitleCase (Uppercase first letter) 

import point 
import random
import turtle
import pygame

#1. Look in current file/module 
#2. Look in python installed modules 
#3. Look in python library 

pygame.init()
display = pygame.display.set_mode()
p1 = point.LED(x=100, y=100 )

points = []
for p in range(20):
   x = random.randint(0,100)
   y = random.randint(0,100)
   p = point.LED(x,y)
   p.random_color()
   points.append(p)
   pygame.draw.circle(display, p.color, (p.rect.x, p.rect.y), p.radius)

while 1:
    pygame.display.flip()
    pygame.time.wait(4000)
    break


#print(p1.xcoor, p1.ycoor, p1.color, type(p1), id(p1))
#p2 = point.Point()
#print(p2.xcoor, p2.ycoor, p2.color, type(p2), id(p2))

#t = turtle.Turtle()
#for p in points: 
    #p.random_color() #Putting in p as the first argument 
  #  t.color(p.color)
   # t.goto(p.xcoor, p.ycoor)

#turtle.Screen().exitonclick()