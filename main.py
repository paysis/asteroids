import pygame
import constants
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)

    # game objects
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update
        for u in updatables:
            u.update(dt)

        # collision check
        for a in asteroids:
            if a.overlaps(player):
                print("Game over!")
                sys.exit()
            
            for s in shots:
                if a.overlaps(s):
                    s.kill()
                    a.split()

        # render
        screen.fill((0,0,0))

        for d in drawables:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()