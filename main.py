# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)    
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        

        #Limit Framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
