""" 
Ce fichier définit les constantes du jeu qui ne sont pas
modifiés"""
import pygame

class Gameconfig:
    BACKGROUND_LEVEL1 = None
    LARGEUR_LEVEL1 = 344 #344
    LONGUEUR_LEVEL1 = 675 #675
    WINDOW_H = 344
    WINDOW_W = 675
    BACKGROUND_LEVEL2 = None
    BACKGROUND_LEVEL3 = None
    STANDING_IMG = None
    Y_PLATEFORM = 285
    PLAYER_W = 40 
    PLAYER_H = 64 
    DT = 0.5
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT
    GRAVITY = 7.81
    FORCE_JUMP = -100
    PRINCESSE = None
    STANDING_MASK = None
    WALK_RIGHT_IMG = []
    WALK_LEFT_IMG = []
    STANDING_IMG = []
    WALK_RIGHT_MASKS = [] 
    WALK_LEFT_MASKS = []
    NB_FRAMES_PER_SPRITE_PLAYER = 5
    D_SEUIL = -2
    seuil_max = -1800
    
    def init():
        Gameconfig.BACKGROUND_LEVEL1 = pygame.image.load("../img_file/niv.png")
        Gameconfig.BACKGROUND_LEVEL2 = pygame.image.load("../img_file/level2.jpg")
        Gameconfig.BACKGROUND_LEVEL3 = pygame.image.load("../img_file/level3.jpeg")
        Gameconfig.WALK_RIGHT_IMG = [ 
                                    pygame.image.load("../img_file/princesseright1.png").convert_alpha(),
                                    pygame.image.load('../img_file/princesseright2.png').convert_alpha(),
                                    pygame.image.load('../img_file/princesseright3.png').convert_alpha(),
                                    pygame.image.load('../img_file/princesseright4.png').convert_alpha(),
                                    pygame.image.load('../img_file/princesseright5.png').convert_alpha(),
                                    pygame.image.load('../img_file/princesseright6.png').convert_alpha(),
                                    pygame.image.load('../img_file/princesseright7.png').convert_alpha()]
        
        Gameconfig.WALK_LEFT_IMG = [
                                    pygame.image.load("../img_file/princesseleft1.png").convert_alpha(),
                                    pygame.image.load('../img_file/princesseleft2.png').convert_alpha(),
                                    pygame.image.load('../img_file/princesseleft3.png').convert_alpha(),
                                    pygame.image.load('../img_file/princesseleft4.png').convert_alpha(),
                                    pygame.image.load('../img_file/princesseleft5.png').convert_alpha(),
                                    pygame.image.load('../img_file/princesseleft6.png').convert_alpha(),
                                    pygame.image.load('../img_file/princesseleft7.png').convert_alpha()]
        
        
        Gameconfig.STANDING_IMG = [
                                    pygame.image.load('../img_file/princesseright1.png').convert_alpha()]
        
        Gameconfig.WALK_RIGHT_MASKS = [] 
        Gameconfig.WALK_LEFT_MASKS = []
        for im in Gameconfig.WALK_RIGHT_IMG : 
            Gameconfig.WALK_RIGHT_MASKS.append(pygame.mask.from_surface(im)) 
        for im in Gameconfig.WALK_LEFT_IMG :
            Gameconfig.WALK_LEFT_MASKS.append(pygame.mask.from_surface(im))
        Gameconfig.STANDING_MASK = [pygame.mask.from_surface(Gameconfig.STANDING_IMG[0])]