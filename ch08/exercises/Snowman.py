import pygame
import random

class Snowman(pygame.sprite.Sprite): #Making it a sprite class to get the functionality from pygae
    def __init__(self, x, y, img="assets/snowman.png"):
        super().__init__() #Needed since we are inheriting sprite class

        self.image = pygame.image.load(img) #Has to be called self.image and then this will create hitbox immediately 
        self.rect = self.image.get_rect() #Get rectangle
        self.rect.x = x #Get coordinates 
        self.rect.y = y #Get coordinates

    def update(self):
        self.rect.y += random.randinit(-10,10)
        self.rect.x += random.randinit(-10,10)