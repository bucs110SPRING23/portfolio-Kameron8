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
hitbox_width = int(width / 2)
hitbox_height = int(height)

#pygame.Rect(x, y, width, height) (x,y) are the starting coordinates while width and height is the size of the rectangle 


hitboxes = {
    "Gold": pygame.Rect(0,0, hitbox_width, hitbox_height),
    "Slate Blue": pygame.Rect(350,0, hitbox_width, hitbox_height),
}


#Define hitbox colors
colors = {
    "Gold": "Gold",
    "Slate Blue": "Slate Blue",
}

order = list(hitboxes.keys())
prediction = []
predicttext = font.render("Pick Which Color Will Win" , True, "white")

while 1:
    pygame.event.get()
    screensize = pygame.display.get_window_size()  
    pygame.draw.rect(window, "Gold", (0,0, hitbox_width, hitbox_height))
    pygame.draw.rect(window, "Slate Blue", (350,0, hitbox_width, hitbox_height)) 
    pygame.display.flip()
    pygame.draw.rect(window, "black", (150,300, 425,40) )
    window.blit(predicttext, (150,300))
    pygame.display.flip()
    pygame.time.delay(5000)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if hitboxes["Gold"].collidepoint(event.pos):
                prediction.append("Gold")
                window.fill("AntiqueWhite2")
            elif hitboxes["Slate Blue"].collidepoint(event.pos):
                prediction.append("Violet")
                window.fill("AntiqueWhite2")
        

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
        text1 = font.render("Gold Wins!" , True, "white")
        winner = ["Gold"]

    elif violetscore > goldscore:
        text1 = font.render("Violet Wins!" , True, "white")
        winner = ["Violet"]

    else: 
        text1 = font.render("It's a Tie!" , True, "white")
        winner = ["Neither"]

    
    
    if prediction == winner: 
        text2 = font.render("Your Prediction Was Correct!", True, "white")
    elif prediction != winner:
        text2 = font.render("Your Prediction Was Wrong!", True, "White")

   
    pygame.draw.rect(window, "Black", (275,300,200,40))
    pygame.draw.rect(window, "Black",(175,340, 475,40) )
    window.blit(text1, (275,300))
    window.blit(text2, (175,340))
    pygame.display.flip()
    pygame.time.wait(4000)

    

    break

