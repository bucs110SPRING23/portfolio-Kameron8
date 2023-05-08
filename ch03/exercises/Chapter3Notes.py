#if True: 
   # print("True")


#No matter what only one statement will run 
#x = "a"
#if x < "y":
   # print("yup")
#elif x < "m": 
    #print("nope")


# Events- Whenever a user interacts with a window or a screen and are all handled by the operating system 
## Your program --> Operating system --> Anything happening? 
# If OS shows an event happened --> Operation can happen 
# Trying to connect actions/events to algorithms 

#Types of Events: Mouse click and key presses 
#Sub-events Right/Left click, particular keys on keyboard 

## Simplified Simon Says 

import pygame 
import random

pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)

while 1:
    screen = pygame.display.set_mode()
    for color in colors:
        screen.fill(color)
        pygame.display.flip()
        pygame.time.wait(1000)

        screen.fill("black")
        pygame.display.flip()
        pygame.time.wait(500)

    
    message = """
        Simon says:
        UP: RED
        DOWN: BLUE
        LEFT: GREEN
        RIGHT: YELLOW

        click on the window, enter sequence, then press enter
    """

    response = input(message)
    user_sequence = []
    for event in pygame.event.get(): #Allowing us to access events from user
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill("red")
                user_sequence.append("red")
            elif event.key == pygame.K_DOWN:
                screen.fill("blue")
                user_sequence.append("blue")
            elif event.key == pygame.K_LEFT:
                screen.fill("green")
                user_sequence.append("green")
            elif event.key == pygame.K_RIGHT:
                screen.fill("yellow")
                user_sequence.append("yellow")
    

    if user_sequence == colors: 
        print("Correct: You win!")
    else:
        print("Wrong: Were you even paying attention?")

    break

  
