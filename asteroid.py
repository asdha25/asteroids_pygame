import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0, 0)

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_angle = random.uniform(20, 50)
    vector1 = self.velocity.rotate(random_angle)
    vector2 = self.velocity.rotate(-random_angle)

    new_radius = self.radius - ASTEROID_MIN_RADIUS

    faster_vector1 = vector1 * 1.2
    faster_vector2 = vector2 * 1.2

    asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

    asteroid1.velocity = faster_vector1
    asteroid2.velocity = faster_vector2