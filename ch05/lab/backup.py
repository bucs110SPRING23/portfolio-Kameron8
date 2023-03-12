
import pygame

pygame.init()

window = pygame.display.set_mode()
flipped_screen = pygame.transform.flip(window,False,True)
width, height = flipped_screen.get_size()
finalscreen = pygame.transform.scale(flipped_screen, (width * 5, height * 5))

inputvalues = []
outputvalues = []

def threenp1(n):
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0: #If n is even
            n = int(n/2)
        else:
            n = int(3*n+1)
    return count 

def threenp1range(a): #Get the number of itrerations to reach 1 for all values from two until the upper limit
    list1 = list(range(2,a+1))
    n = 0
    for _ in list1:
        count = 0 
        inputvalues.append(list1[n])
        while list1[n] > 1.0:
            count += 1
            if list1[n] % 2 == 0: #If number is even
                 list1[n] = int(list1[n]/2)
            else:
                list1[n] = int(3*list1[n]+1)
        outputvalues.append(count)
        n+=1
    objs_in_sequence = dict(zip(inputvalues,outputvalues))
    coordinates = list(objs_in_sequence.items())
    return coordinates
        

def graph_coordinates(coordinates): 
    while 1: 
        pygame.event.get()
        window.blit(finalscreen, (0,0))
        finalscreen.fill("White")
        pygame.draw.lines(finalscreen, "Orange", False, coordinates)
        pygame.display.flip()
        pygame.time.wait(5000)
        break



def main():
    print(threenp1(int(input(": "))))
    graph_coordinates(threenp1range(int(input(": "))))

main()