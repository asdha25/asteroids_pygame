import pygame
import sys
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  print("Starting Asteroids!")
  clock = pygame.time.Clock()
  shot = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  Shot.containers = (shot, updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidField = AsteroidField()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  while True:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill("black")
    updatable.update(dt)
    for asteroid in asteroids:
      if player.collide(asteroid):
        print("Game Over!")
        sys.exit()
    
    for asteroid in asteroids:
      for bullet in shot:
        if bullet.collide(asteroid):
          bullet.kill()
          asteroid.split()

    for entity in drawable:
      entity.draw(screen)
    pygame.display.flip()
   

if __name__ == "__main__":
  main()

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")