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
    

def draw_text(screen, text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def main():
    screen = init_game()
    clock = pygame.time.Clock() 

    my_font1 = pygame.font.SysFont('Arial',25)
    # my_text1 = my_font1.render("Katelyn", True)
    my_font2 = pygame.font.SysFont('Courier New',50)


    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) 
        


        draw_text(screen, "Kateyln", my_font1, config.RED, 150, 425)
        draw_text(screen, "Keily", my_font2, config.GREEN, 450, 230)

        pygame.display.flip()

        clock.tick(config.FPS) 

    pygame.quit()

    sys.exit()
if __name__ == "__main__":
    main()