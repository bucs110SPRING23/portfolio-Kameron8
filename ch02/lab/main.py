# Part A
# Race 1 

import random 
import turtle 

window = turtle.Screen()

pen1 = turtle.Turtle()
pen2 = turtle.Turtle()

pen1.color("Red")
pen1.shape("turtle")
pen2.color("Green")
pen2.shape("turtle")

pen1.up()
pen1.goto(-100,20)
pen1.down()
pen2.up()
pen2.goto(-100,-20)
pen2.down()

pen1.forward(random.randrange(101)) #Am i hard coding random variables or using random.randrange?
pen2.forward(random.randrange(101)) #Am i hard coding random variables or using random.randrange?

pen1.goto(-100,20)
pen2.goto(-100,-20)

window.exitonclick()

#Race 2

import random #How should I format it to allow both races to happen
import turtle #Right now it is set up so that I can run this by itself assuming race 1 isn't already in the code 

window = turtle.Screen()

pen1 = turtle.Turtle()
pen2 = turtle.Turtle()

pen1.color("Red")
pen1.shape("turtle")
pen2.color("Green")
pen2.shape("turtle")

pen1.up()
pen1.goto(-100,20)
pen1.down()
pen2.up()
pen2.goto(-100,-20)
pen2.down()

x = random.randrange(11)
y = random.randrange(11)


for i in range(10):
    pen1.forward(x)
    pen2.forward(y)

pen1.goto(-100,20)
pen2.goto(-100,-20)

window.exitonclick()

# Part B 

import pygame 
import math 

pygame.init()

while 1:
    window = pygame.display.set_mode()

    points = [] #Triangle Start
    num_sides = 3
    side_length = 100
    xpos = 800
    ypos = 400
    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = int(xpos + side_length * math.cos(radians))
        y = int(ypos + side_length * math.sin(radians))
        points.append([x,y])
        
    pygame.event.get()
    window.fill("White")
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.draw.polygon(window, "Red", points)
    pygame.display.flip()
    pygame.time.wait(1000) 
    window.fill("White")
    pygame.display.flip() #Triangle end
    
    points2 = [] #Square Start
    num_sides = 4
    side_length = 100
    xpos = 800
    ypos = 400

    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = int(xpos + side_length * math.cos(radians))
        y = int(ypos + side_length * math.sin(radians))
        points2.append([x,y])
    
    window.fill("White")
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.draw.polygon(window, "Orange", points2)
    pygame.display.flip()
    pygame.time.wait(1000) 
    window.fill("White")
    pygame.display.flip() #Square end

    points3 = [] #Hexagon Start
    num_sides = 6
    side_length = 100
    xpos = 800
    ypos = 400

    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = int(xpos + side_length * math.cos(radians))
        y = int(ypos + side_length * math.sin(radians))
        points3.append([x,y])
    
    window.fill("White")
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.draw.polygon(window, "Yellow", points3)
    pygame.display.flip()
    pygame.time.wait(1000) 
    window.fill("White")
    pygame.display.flip() #Hexagon end
    
    points4 = [] #Icosagon Start
    num_sides = 20
    side_length = 100
    xpos = 800
    ypos = 400

    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = int(xpos + side_length * math.cos(radians))
        y = int(ypos + side_length * math.sin(radians))
        points4.append([x,y])
    
    window.fill("White")
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.draw.polygon(window, "Green", points4)
    pygame.display.flip()
    pygame.time.wait(1000) 
    window.fill("White")
    pygame.display.flip() #Icosagon end

    points5 = [] #Hectagon Start
    num_sides = 100
    side_length = 100
    xpos = 800
    ypos = 400

    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = int(xpos + side_length * math.cos(radians))
        y = int(ypos + side_length * math.sin(radians))
        points5.append([x,y])
    
    window.fill("White")
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.draw.polygon(window, "Blue", points5)
    pygame.display.flip()
    pygame.time.wait(1000) 
    window.fill("White")
    pygame.display.flip() #Hectagon end

    points6 = [] #Circle Start
    num_sides = 360
    side_length = 100
    xpos = 800
    ypos = 400

    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = int(xpos + side_length * math.cos(radians))
        y = int(ypos + side_length * math.sin(radians))
        points6.append([x,y])
    
    window.fill("White")
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.draw.polygon(window, "Purple", points6)
    pygame.display.flip()
    pygame.time.wait(1000) 
    window.fill("White")
    pygame.display.flip() #Circle end
    break
