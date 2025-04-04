import pygame
from constants import *
import player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    frame_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_instance = player.Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    while True:
        screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()        

        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                return
        dt = frame_clock.tick(60) / 1000

if __name__ == "__main__":
    main()