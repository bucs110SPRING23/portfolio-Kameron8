import random
import pygame 

pygame.init()

screen = pygame.display.set_mode()
width, height = screen.get_window_size() #Works because of tuples 

hitbox_width = width / 2 #Half the screen
hitbox_height = height / 2 #Half the screen again making a hitbox just a quarter of the screen

#pygame.Rect- different from draw rectangle, stores x and y coordinates aka width and height of a hitbox
# Rectangles do NOT track visuals, only location

#pygame.Rect(x, y, width, height) (x,y) are the starting coordinates while width and height is the size of the rectangle 

#Sets up the hitboxes byt does not position them 
hitboxes = {
    "red": pygame.Rect(0,0, hitbox_width, hitbox_height),
    "green": pygame.Rect(0,0, hitbox_width, hitbox_height),
    "blue": pygame.Rect(0,0, hitbox_width, hitbox_height),
    "purple": pygame.Rect(0,0, hitbox_width, hitbox_height),
}

#Positions hitboxes
hitboxes["blue"].topleft = hitboxes["red"].topright
hitboxes["green"].bottomleft = hitboxes["red"].bottomright
hitboxes["purple"].topleft = hitboxes["red"].bottomright

#Define hitbox colors 
main_colors = {
    "red": (200,0,0),
    "green": (0,200,0),
    "blue": (0,0,200),
    "purple": (200,0,200)
}
highlight_colors = {
    "red": (200,0,0),
    "green": (0,200,0),
    "blue": (0,0,200),
    "purple": ()

}
font = pygame.font.SysFont("Arial", 24)

done = False
result = []
turns = 0
order = list(hitboxes.keys())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                random.shuffle(order)
                turns = len(order)
                result = []
                for color in order:
                    for c, hb in hitboxes.items():
                        pygame.draw.rect(screen,main_colors[c], hb) #Drawing hitboxes on the screen
                        pygame.draw.rect(screen,highlight_colors[color], hitboxes[color])
                        pygame.display.flip()
                        pygame.time.wait(2000)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            turns -= 1 #same as turns = turns - 1
            if hitboxes["red"].collidepoint(event.pos):
                result.append("red")
            elif hitboxes["green"].collidepoint(event.pos):
                result.append("green")
            elif hitboxes["blue"].collidepoint(event.pos):
                result.append("blue")
            elif hitboxes["purple"].collidepoint(event.pos):
                result.append("purple")
    if turns == 0:
        if result == order: 
            font.render("You win!", True, "white")
        else: 
            font.render("You win!", True, "white")
    screen.fill ((0,0,0))

    for c, hb in hitboxes.items():
        box = pygame.draw.rect(screen,c,hb)
        screen.blit(box, hb)

    

