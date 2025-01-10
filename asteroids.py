
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import copy
import pygame
import random 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(0,0, new_radius)
        ast1.position = copy.deepcopy(self.position)
        ast1.velocity = vector1
        ast2 = Asteroid(0,0, new_radius)
        ast2.position = copy.deepcopy(self.position)
        ast2.velocity = vector2