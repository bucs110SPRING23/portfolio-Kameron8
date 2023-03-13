#Part A 

import pygame 
import math
import random

pygame.init()
num_sides = 360
side_length = 350
xpos = 350
ypos = 350
points = [] 

while 1:
    window = pygame.display.set_mode(size = (700, 700))
    pygame.event.get()
    screensize = pygame.display.get_window_size()

    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = int(xpos + side_length * math.cos(radians))
        y = int(ypos + side_length * math.sin(radians))
        points.append([x,y])
    
    window.fill("AntiqueWhite2")
    pygame.display.flip()
    pygame.draw.polygon(window, "SkyBlue2", points)
    pygame.display.flip()
    pygame.draw.line(window,"Black",[350,700], [350,0])
    pygame.display.flip()
    pygame.draw.line(window,"Black", [0,350], [700,350])
    pygame.display.flip()
    pygame.time.wait(2000)

    for _ in range(10):
        a = random.randrange(0,701)
        b = random.randrange(0,701)
        distance_from_center = math.hypot(a-350,b-350)
        is_in_circle = distance_from_center <= 350
        if is_in_circle == True:
            pygame.draw.circle(window,"Green", [a,b],10)
            pygame.display.flip()
            pygame.time.wait(1000)
        else:
            pygame.draw.circle(window,"Red", [a,b], 10)
            pygame.display.flip()
            pygame.time.wait(1000)
    break

    