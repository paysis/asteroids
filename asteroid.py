import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def __spawn_smaller_asteroid(self, new_angle, velocity_scale=1.0):
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast.velocity = self.velocity.rotate(new_angle)
        new_ast.velocity *= velocity_scale

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        self.__spawn_smaller_asteroid(angle, 1.2)
        self.__spawn_smaller_asteroid(-angle, 1.2)
        