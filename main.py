import pygame    
import numpy as np
import time

# Colors

BG = (30, 30, 30)
WHITE = (250, 250, 250)

# Screen size variable

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 800

number_cell_x = 25
number_cell_y = 25

dim_cell_x = SCREEN_WIDTH // number_cell_x
dim_cell_y = SCREEN_HEIGTH // number_cell_y

def game_loop():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    clock = pygame.time.Clock()
    cell_state = np.zeros((number_cell_y, number_cell_x))
    running = True  


    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    draw_cell(screen, mouse_position, cell_state) 

        screen.fill(BG)
        draw_grid(screen)
        draw_active_cells(screen, cell_state) 
        pygame.display.flip()
        clock.tick(60)

def draw_cell(screen, coords, cell_state):
    
    x = coords[0] // dim_cell_x
    y = coords[1] // dim_cell_y
    
    if cell_state[y, x] == 0:
        cell_state[y, x] = 1
    else:
        cell_state[y, x] = 0
    

def draw_active_cells(screen, cell_state):
    for y in range(number_cell_y):
        for x in range(number_cell_x):
            if cell_state[y, x] == 1:
                pygame.draw.rect(screen, WHITE, (x*dim_cell_x, y*dim_cell_y, dim_cell_x, dim_cell_y))



def draw_grid(screen): 
    for y in range(0, number_cell_y):
        for x in range(0, number_cell_x):  
            cell_coords = [
                (x * dim_cell_x, y * dim_cell_y),
                ((x + 1) * dim_cell_x, y * dim_cell_y),
                ((x + 1) * dim_cell_x, (y + 1) * dim_cell_y),
                (x * dim_cell_x, (y + 1) * dim_cell_y)
            ]
            pygame.draw.polygon(screen, WHITE, cell_coords, 1) 



if __name__ == "__main__":

    game_loop()