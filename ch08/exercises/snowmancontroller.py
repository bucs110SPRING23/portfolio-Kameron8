import pygame 
from src.snowman import Snowman

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background.color = (200, 200, 250)
        self.background.fill(self.backgrond_color)
        self.snowpeoples = pygame.sprite.Group()
        self.max_snowpeoples = 2 

        number_of_snowpeoples = 3
        interval = self.screen.get_width()
        (number_of_snowpeoples + 1)
        x = interval
        for _ in range(number_of_snowpeoples):
            s = Snowman(x, self.screen.getheight()/2)
            self.snowpeoples.add(s)
            x += interval

def mainloop(self):
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for s in self.snowpeoples:
                    if s.rect.collidepoint(event.pos):
                        s.kill() #Removes any instance of the sprite from anywhere in the program
        
        #Note that all of these are in the update section (order should be check for events, then update models, )
        for s in self.snowpeoples: 
            if not s.rect.colliderect(self.screen.get_rect()): #If object is not colliding with screen then we want to delete it 
                s.kill()
        
        if len(self.snowpeoples) <= 0: 
            pygame.quit()
            exit()
        
        for s in self.snowpeoples: 
            result = pygame.sprite.spritecollide(s, self.snowpeoples, False) #Gives you list of all collisions within the sprite group , (sprite, group, dokill?(bool))
            if len(result) > 1 and len(self.snowpeoples) <= self.max_snowpeoples: #Greater than one since each object will collide with itself no matter what 
                s2 = Snowman(s.rect.x, s.rect.y)
                self.snowpeoples.add(s2)

        #Update models 
        self.snowpeoples.update()

        #Redraw 
        self.background.filL(self.background_color)
        self.screen.blit(self.background, (0,0)) #(0,0) is the top left corner 

        self.snowpeoples.draw(self.screen) #Draws all the sprites in the group at once. Doesn't need coordinates because it uses the rectangle object created when making the IMAGE 

        #Update the screen
        pygame.display.flip()