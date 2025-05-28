import pygame    
import numpy as np
import time

import os
os.environ['SDL_VIDEO_X11_FORCE_EGL'] = '1'

# Colors

BG = (30, 30, 30)
WHITE = (250, 250, 250)

# Screen size variable

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 800

number_cell_x = 50
number_cell_y = 50

dim_cell_x = SCREEN_WIDTH // number_cell_x
dim_cell_y = SCREEN_HEIGTH // number_cell_y

def game_loop():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    clock = pygame.time.Clock()
    cell_state = np.zeros((number_cell_y, number_cell_x))
    running = True  
    playing = False

    # Funciones que se ejecutan una sola vez (de generacion)

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_position = pygame.mouse.get_pos()
            #     draw_cell(screen, mouse_position, cell_state)

            elif pygame.mouse.get_pressed()[0]:
                mouse_position = pygame.mouse.get_pos()
                draw_cell(screen, mouse_position, cell_state)

            elif pygame.mouse.get_pressed()[2]:
                mouse_position = pygame.mouse.get_pos()
                delete_cell(screen, mouse_position, cell_state)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if playing == True:
                        playing = False
                    else: 
                        playing = True
            
                if event.key == pygame.K_BACKSPACE:
                    cell_state = clear_grid()
                    screen.fill(BG)
                    draw_grid(screen)
                    draw_active_cells(screen, cell_state)
                    pygame.display.flip()


        if playing:
            cell_state = update_game(cell_state)
            time.sleep(0.05)              

        screen.fill(BG)
        draw_grid(screen)
        draw_active_cells(screen, cell_state)
        pygame.display.flip()
        clock.tick(300)

# Me genera y dibueja la celula en la pantalla.
def draw_cell(screen, coords, cell_state):

    x = coords[0] // dim_cell_x
    y = coords[1] // dim_cell_y
    
    cell_state[y, x] = 1 
    

def delete_cell(screen, coords, cell_state):
    x = coords[0] // dim_cell_x
    y = coords[1] // dim_cell_y

    cell_state[y, x] = 0
    

def draw_active_cells(screen, cell_state):
    for y in range(number_cell_y):
        for x in range(number_cell_x):
            if cell_state[y, x] == 1:
                pygame.draw.rect(screen, WHITE, (x*dim_cell_x, y*dim_cell_y, dim_cell_x, dim_cell_y))
                
def clear_grid():
    return np.zeros((number_cell_y, number_cell_x))

def update_game(cell_state):
    new_state = np.copy(cell_state)  
    rows, cols = cell_state.shape
    
    for y in range(rows):
        for x in range(cols):
            neighbors = count_neighbors(cell_state, x, y)
            
            if cell_state[y, x] == 1:  
                if neighbors < 2 or neighbors > 3:
                    new_state[y, x] = 0
                else: 
                    print(f"La celula va a seguir viva")             
            else:  
                if neighbors == 3:
                    new_state[y, x] = 1  
                    print(f"La celula va a NACER")
                    
    
    return new_state


def count_neighbors(grid, x: int, y: int) -> int:

    neighbor_cells = [
        (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
        (x, y - 1),                   (x, y + 1),
        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
    ]
    count = 0

    for x,y in neighbor_cells:
        if x >= 0 and y >= 0:
            try:
                count += grid[y, x]
            except:
                pass
    return count




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