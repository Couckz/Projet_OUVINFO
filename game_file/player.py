""" 
contient la classe qui gère le joueur"""
import pygame
from gameconfig import Gameconfig

class Player(pygame.sprite.Sprite):
    LEFT = -1
    RIGHT = 1
    NONE = 0
    
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, Gameconfig.Y_PLATEFORM, Gameconfig.PLAYER_H, Gameconfig.PLAYER_W)
        self.sprite_count = 0
        self.direction = Player.NONE 
        self.image = Player.IMAGES[self.direction][self.sprite_count//Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.mask = Player.MASKS[self.direction][self.sprite_count//Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.vx = 0
        self.vy = 0
        
    def draw(self, window):
        window.blit(self.image, self.rect.topleft)
    
    def advance_state(self, next_move):
        fx = 0
        fy = 0
        if next_move.left:
            fx = Gameconfig.FORCE_LEFT
            self.direction = Player.LEFT
        elif next_move.right:
            fx = Gameconfig.FORCE_RIGHT    
            self.direction = Player.RIGHT 
            
        x,y = self.rect.topleft
        vx_min = -x/Gameconfig.DT
        vx_max = (Gameconfig.WINDOW_W-Gameconfig.PLAYER_W-x)/Gameconfig.DT
        self.vx = fx*Gameconfig.DT
        self.vx = min(self.vx, vx_max)
        self.vx = max(self.vx, vx_min)
        
        if next_move.jump:
            fy = Gameconfig.FORCE_JUMP

        if self.on_ground():
            self.vy = fy*Gameconfig.DT
        else:
            self.vy = self.vy+Gameconfig.GRAVITY*Gameconfig.DT
        vy_max = (Gameconfig.Y_PLATEFORM-Gameconfig.PLAYER_H-y)/Gameconfig.DT
        self.vy = min(self.vy, vy_max)
        self.rect = self.rect.move(self.vx*Gameconfig.DT, self.vy*Gameconfig.DT)
        self.sprite_count+=1
        if self.sprite_count >= Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER*len(Player.IMAGES[self.direction]) : 
            self.sprite_count=0
            self.image = Player.IMAGES[self.direction][self.sprite_count//Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER]
            self.mask = Player.MASKS[self.direction][self.sprite_count//Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER]

    def on_ground(self):
        if self.rect.bottom == Gameconfig.Y_PLATEFORM:
            return True
        return False

    def init_sprites():
        Player.IMAGES = {Player.LEFT : Gameconfig.WALK_LEFT_IMG, Player.RIGHT : Gameconfig.WALK_RIGHT_IMG, Player.NONE : Gameconfig.STANDING_IMG}
        Player.MASKS = {Player.LEFT : Gameconfig .WALK_LEFT_MASKS, Player.RIGHT : Gameconfig.WALK_RIGHT_MASKS, Player.NONE : Gameconfig.STANDING_MASK}
