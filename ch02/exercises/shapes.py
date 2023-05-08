import pygame 

pygame.init()

radius = 100
while 1:
    pygame.event.get()
    screen = pygame.display.set_mode()
    dimensions = screen.get_size()
    starting_point = [dimensions[0] // 2, dimensions[1] // 2]
    screen.fill("dark blue")
    for _ in range(3): #Can expand the number of snowballs in the snowman
        pygame.draw.circle(screen, "white", starting_point, radius)
        starting_point[1] = starting_point[1] - radius #Moves the y axis up by the value of the radius 
        radius = radius // 2 #Make each subsequent snowball smaller than the previous
        starting_point[1] = starting_point[1] - radius
        pygame.display.flip()
        pygame.time.wait(1000)
    pygame.time.wait(2000)
    break
