import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)



    def update(self, dt):
        self.position += self.velocity * dt

       
      
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Create two smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = self.velocity.rotate(random.randint(-30, 30)) * 1.2
        new_asteroid2.velocity = self.velocity.rotate(random.randint(30, 60)) * 1.2
        new_asteroid1.add(self.containers[0])
        new_asteroid2.add(self.containers[0])
        return new_asteroid1, new_asteroid2