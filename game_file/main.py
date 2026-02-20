import pygame

def gameloop(window):
    quitting = False
    while not quitting : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True

    
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((1280, 720))
    gameloop(window)
    pygame.quit()
    quit()