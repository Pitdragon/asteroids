import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FPS = 60
    # Initialize the clock
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()








if __name__ == "__main__":
    main()