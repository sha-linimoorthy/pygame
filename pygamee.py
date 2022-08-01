import pygame
import os


WIDTH=900
HEIGHT=500
BIN =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game for gamers")
COLOR=(120,120,0)

FPS=60
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets','spaceship_yellow.png'))

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets','spaceship_red.png'))





def draw_window():
    BIN.fill(COLOR)
    BIN.blit(YELLOW_SPACESHIP_IMAGE,())
    pygame.display.update()
    

def main():
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                
        draw_window()

    pygame.quit()


if __name__=="__main__":
    main()
            
