import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FPS = 60

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)
    
    # Initialize the clock
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroidfield = AsteroidField()
    
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       
        screen.fill(BLACK)
        updatables.update(dt)

        # Check for collisions between asteroids and shots
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
                    break
                    
        # Check for collisions
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game Over!")
                running = False
                break
        # Draw the player and asteroids
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        dt = clock.tick(FPS) / 1000.0

    pygame.quit()








if __name__ == "__main__":
    main()