import pygame 
import math
import random

pygame.init()
num_sides = 360
side_length = 350
xpos = 350
ypos = 350
points = [] 
goldscore = 0
violetscore = 0
font = pygame.font.Font(None, 48)
window = pygame.display.set_mode(size = (700, 700))
width, height = pygame.display.get_window_size()
hitbox_width = width / 2
hitbox_height = height

hitboxes = {
    "Gold": pygame.Rect(0,0, hitbox_width, hitbox_height),
    "Slate Blue": pygame.Rect(0,0, hitbox_width, hitbox_height),
}

hitboxes["Gold"].left = hitboxes["Slate Blue"].right


while 1:
    pygame.event.get()
    screensize = pygame.display.get_window_size()
    hitboxes["Gold"].left = hitboxes["Slate Blue"].right
    pygame.display.flip()

    for i in range(num_sides): #Generating points for circle of dartboard
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = int(xpos + side_length * math.cos(radians))
        y = int(ypos + side_length * math.sin(radians))
        points.append([x,y])
    
    #Structure of Dart Board 
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
            pygame.draw.circle(window,"Gold", [a,b],10)
            pygame.display.flip()
            pygame.time.wait(1000)
            goldscore = goldscore + 1
        
        else:
            pygame.draw.circle(window,"Red", [a,b], 10)
            pygame.display.flip()
            pygame.time.wait(1000)
        
        c = random.randrange(0,701)
        d = random.randrange(0,701)
        distance_from_center = math.hypot(c-350,d-350)
        is_in_circle = distance_from_center <= 350
        if is_in_circle == True:
            pygame.draw.circle(window,"Slate Blue", [c,d],10)
            pygame.display.flip()
            pygame.time.wait(1000)
            violetscore = violetscore + 1
        
        else:
            pygame.draw.circle(window,"Red", [c,d], 10)
            pygame.display.flip()
            pygame.time.wait(1000)

    if goldscore > violetscore: 
        text = font.render("Gold Wins!" , True, "white")

    elif violetscore > goldscore:
        text = font.render("Violet Wins!" , True, "white")

    else: 
        text = font.render("It's a Tie!" , True, "white")

   
    pygame.draw.rect(window, "black", (275,300,200,40))
    window.blit(text, (275,300) )
    pygame.display.flip()
    pygame.time.wait(4000)

    break
