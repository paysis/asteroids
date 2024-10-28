import pygame
import constants
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)

    # game objects
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update
        for u in updatables:
            u.update(dt)

        # render
        screen.fill((0,0,0))

        for d in drawables:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()