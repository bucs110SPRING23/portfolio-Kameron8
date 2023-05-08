
import pygame

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
    
    inputvalues = []
    outputvalues = []

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
    window = pygame.display.set_mode((500,500))
    font = pygame.font.Font(None, 25)
    y = []

    while 1: 
        pygame.event.get()
        window.fill("White")
        pygame.draw.lines(window, "Orange", False, coordinates)
        for elem in coordinates:
            if type(elem[1]) == tuple:
                y.append(max(elem[1]))
            else: 
                y.append(elem[1])

        max_y = str(max(y))
        msg = font.render(max_y , True, "Dark Blue")
        msg2 = font.render("Max Number of Iterations:", True, "Dark Blue")
        window.blit(msg2, (50,150))
        window.blit(msg, (300,150))
        pygame.display.flip()
        pygame.time.wait(3000)
        break




def main():
    pygame.init()
    print(threenp1(int(input(": "))))
    coordinates = threenp1range(int(input(": ")))
    print(coordinates)
    graph_coordinates(coordinates)


main()