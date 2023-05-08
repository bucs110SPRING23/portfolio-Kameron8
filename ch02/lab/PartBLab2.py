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
