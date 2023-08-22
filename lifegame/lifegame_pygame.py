import time
import pygame
import numpy as np

COLOR_BG = (10,10,10) # BLACK
COLOR_GRID = (40,40,40) # GRAY
COLOR_DIE_NEXT = (170,170,170) # LIGHT GRAY
COLOR_ALIVE_NEXT = (255,255,255) # WHITE

def update(screen, cells, size, with_progress = False):
    updated_cells = np.zeros((cells.shape[0],cells.shape[1])) # create a new array to store the updated cells

    for row,col in np.ndindex(cells.shape): 
        alive = np.sum(cells[row-1:row+2,col-1:col+2]) - cells[row,col] # count the number of alive cells around the current cell
        color = COLOR_BG if cells[row,col] == 0 else COLOR_ALIVE_NEXT

        if cells[row,col] == 1 :
            if alive < 2 or alive > 3: 
                if with_progress :
                    color = COLOR_DIE_NEXT
            elif 2<=alive <=3:
                updated_cells[row,col]=1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        else:
            if alive == 3:
                updated_cells[row,col] =1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        pygame.draw.rect(screen, color, (col*size,row*size,size-1,size-1)) # draw the cell

    return updated_cells
  
def main():
    pygame.init()
    screen = pygame.display.set_mode((800,800))

    cells = np.zeros((100,100))
    screen.fill(COLOR_GRID)
    update(screen, cells, 8)

    pygame.display.flip()
    pygame.display.update()

    running = False
    while True : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 8)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 8, pos[0] // 8] = 1 # click 위치설정
                update(screen, cells, 8)
                pygame.display.update()
                    
        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 8, with_progress=True)
            pygame.display.update()

        time.sleep(0.01)

if __name__ == '__main__':
    main()