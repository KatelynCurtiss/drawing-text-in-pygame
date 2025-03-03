# Katelyn Curtiss
# February 12 2025
# Game Code

import pygame
import sys
import config

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
        return True

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    while running:
        running = handle_events()
    screen.fill(config.WHITE) # Use color from config
    pygame.display.flip()

    clock.tick(config.FPS) 
pygame.quit()

sys.exit()
if __name__ == "__main__":
    main()