import pygame    

# Colors

BG = (30, 30, 30)
WHITE = (250, 250, 250)

# Screen size variable

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 640




def game_loop():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    clock = pygame.time.Clock()
    running = True  


    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

      
        screen.fill(BG)

        # RENDER YOUR GAME HERE
        
        draw_grid(15, screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60


def draw_grid(tile_size, screen):
    for v in range(0, SCREEN_WIDTH, tile_size):
        pygame.draw.line(screen, WHITE, (v, 0), (v, SCREEN_HEIGTH))
    for h in range(0, SCREEN_HEIGTH, tile_size):
        pygame.draw.line(screen, WHITE, (0, h), (SCREEN_WIDTH, h))

def check_neighbors():
    pass

if __name__ == "__main__":

    game_loop()