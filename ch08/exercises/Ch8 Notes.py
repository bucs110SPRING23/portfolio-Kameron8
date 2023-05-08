## Use classes to give us a way to organize our code 
## Use "class" for a user-defined type but it is the same thing as a type 
## Also sometimes called a complex type 

## Classes contain data, which is referred to as instance variables 

import turtle

class Num: 
    # Double underscore is called a dunder 
    def __init__(self, n):
        self.data = n #This is the instance variable for Num type objects 
        self.x = "string"
    
    def addone(self): #Using self as 1st parameter makes it a method 
        self.data += 1 

#class Foo: 

    #def __init__(self, x, y, z, a, b, c): 
       # self.x = x 
       # self.y = y #For all of them, instead you can do 

   # def __init__(self,  **kwargs): #Stands for keywrod arguments, allows you to use a dictionary instead 
       # self.__dict__ = kwargs #Can use this to not have to define each instance variables individually 
    
def main():
    
    mynum = Num(7) #Prints a 7 
    mynum2 = Num(9) #Prints a 9 
    mynum3 = {"data":7, "x": "string"}

    print(mynum.data)
    print(mynum2.data)
    #print(mynum3["data"])
    #print(mynum.__dict__)

    mynum.addone()
    print(mynum.data) #Adds one to the value; prints an 8 
    mynum2.addone()
    print(mynum2.data) #Adds one to the value; prints a 10 

   # dictionary = {"x":1, "y":2, "z":3}
    #foo = Foo(**dictionary) #two stars spaces out the data 

   # t = turtle.Turtle() #Creating turtle object from it's __init__ 
  #  t.forward(56)

main()


## Dunders - Double underscores around something, used by python but not you 


## GUI Programs: 
### Everything is put into a class 

#Model - Data 
# view - Display (pygame) 
# Controller - Logic 

#Extent of main: 
#from _____ import Controller 

# def main(): 
#    controller = Controller() 
#    controller.mainloop()


## Need to say from src (source) most likely, all imports are relative to the MAIN not the class you are importing to 

## Sprites - Anything that moves around the screen and/or interact with other things is a sprite 

## Inheritance - #If you have a class. class Bar(Foo) bar gets all of the functionality from foo.  

#If you are going to use pygame.sprites than use the 1st and 3rd lines here 

# class Point(pygame.sprite.Sprite) #You get a lot of extra stuff with the model 
    #def __init__(self, x, y, color, size)
        #super().__init__()

# Needs a self.iage variable which must be a surface object 
## Also needs a rectangle object (get_rect())
### Use this for my final project 


# Hook method (callbacks) 


## Creating a sprite group 
### self.points = pyame.Group() 
### self.points.update() # Updates all of the points at once


### More talk about sprites 

