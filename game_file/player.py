import pygame
from gameconfig import Gameconfig
import time 
from background import BG

class Player(pygame.sprite.Sprite):
    LEFT = -1
    RIGHT = 1
    NONE = 0
    

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, 200, Gameconfig.PLAYER_W, Gameconfig.PLAYER_H)
        self.sprite_count = 0
        self.direction = Player.NONE 
        self.image = Player.IMAGES[self.direction][self.sprite_count//Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.mask = Player.MASKS[self.direction][self.sprite_count//Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.vx = 0
        self.vy = 0
        self.count_cle = 0
        self.on_ground = True
    
    #Sert à l'affichage et gestion du sprite principal du joueur
    def draw(self, window, seuil):
        screen_x = self.rect.x + seuil
        if screen_x < 0:
            screen_x = 0
        if screen_x > Gameconfig.WINDOW_W - Gameconfig.PLAYER_W:
            screen_x = Gameconfig.WINDOW_W - Gameconfig.PLAYER_W
        window.blit(self.image, (screen_x, self.rect.y))
        #pygame.draw.rect(window, (255, 0, 0),(screen_x, self.rect.y, self.rect.width, self.rect.height), 2)

    
    #Récupérer le prochain état du joueur
    def advance_state(self, next_move):
        fx = 0
        fy = 0
        if next_move.left:
            fx = Gameconfig.FORCE_LEFT
            self.direction = Player.LEFT
        elif next_move.right:
            fx = Gameconfig.FORCE_RIGHT    
            self.direction = Player.RIGHT 
        else:
            self.direction = Player.NONE
        x,y = self.rect.topleft
        vx_min = -x/Gameconfig.DT
        vx_max = 1000  
        self.vx = fx*Gameconfig.DT
        self.vx = min(self.vx, vx_max)
        self.vx = max(self.vx, vx_min)
    
        if next_move.jump and self.vy == 0:
            fy = Gameconfig.FORCE_JUMP
            self.vy = fy*Gameconfig.DT
        else:
            self.vy = self.vy+Gameconfig.GRAVITY*Gameconfig.DT  
        
        if self.sprite_count >= Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER*len(Player.IMAGES[self.direction]) : 
            self.sprite_count=0
        time.sleep(0.001)
        self.image = Player.IMAGES[self.direction][self.sprite_count//Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.mask = Player.MASKS[self.direction][self.sprite_count//Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER]
        vy_max = (Gameconfig.Y_PLATEFORM-Gameconfig.PLAYER_H-y)/Gameconfig.DT
        self.vy = min(self.vy, vy_max)
        self.rect = self.rect.move(self.vx*Gameconfig.DT, self.vy*Gameconfig.DT)
        self.sprite_count+=1
        

    #Initialiser les sprites du joueur
    def init_sprites():
        Player.IMAGES = {Player.LEFT : Gameconfig.WALK_LEFT_IMG, Player.RIGHT : Gameconfig.WALK_RIGHT_IMG, Player.NONE : Gameconfig.STANDING_IMG}
        Player.MASKS = {Player.LEFT : Gameconfig .WALK_LEFT_MASKS, Player.RIGHT : Gameconfig.WALK_RIGHT_MASKS, Player.NONE : Gameconfig.STANDING_MASK}
 