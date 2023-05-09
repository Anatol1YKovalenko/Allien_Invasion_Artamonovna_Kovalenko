import pygame as pg
class Ship():
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        
        self.image = pg.transform.scale(pg.image.load("images/ship.png").convert_alpha(),(100,100))
        self.rect = self.image.get_rect()
    
        self.rect.midbottom = self.screen_rect.midbottom 
         
        self.x = float(self.rect.x)

         #Флаги перемещения
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x +=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x -=self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)