# MVC- Model View Controller 
## For GUI Programs 
## Solution to a common problem 
## Design Patterns (solve solutions for programs) (language independent)

# View - Displays things on screen 
    # pygame and turtle both are views

# Controller - Control things on screen, makes everything stay in their lines 
    # Keyboard 

# Model - Contains the data needed 
    # Almost always a class and contains the data for the program 


# View and Model do not talk to eachother, they both have to go through the controller first 

# Skinability - How easy is it to change the visual interface (high skinability = less changes needed)


# Main loop always starts with a while loop - update the display --> show the dislpay  

import pygame
import point


def mainloop():
    while True: 
        points = []
        #event loop 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                point_deleted = False #Flagging variable 
                for p in points: 
                    if p.rect.collidepoint(event.pos): #For each point in the list if it collides with an existing point then 
                        del p #delete that point 
                        point_deleted = True #A point has been deleted 
                if not point_deleted: #cycles through all existing points BEFORE drawing next point 
                    p = point.Point(event.pos)
                    points.append(p)
    

        display.fill("white")
        for p in points: 
            pygame.draw.circle(display, p.color, p.rect.center, p.rect.h / 2)
        pygame.display.flip()

def main():
    pygame.init()
    displa