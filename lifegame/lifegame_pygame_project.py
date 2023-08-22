import time
import pygame
import numpy as np

COLOR_BG = (255,255,255) # white
COLOR_GRID = (170,170,170) # light GRAy
COLOR_DIE_NEXT = (100,100,100) # dark GRAY
COLOR_ALIVE_NEXT = (10,10,10) # black

def update(screen, cells, size, with_progress = False):
    updated_cells = np.zeros(cells.shape) # create a new array to store the updated cells

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
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("lifegame") #게임 이름


    cells = np.zeros((100,100))
    screen.fill(COLOR_GRID)
    update(screen, cells, 8)

    pygame.display.update()

    running = False
    count=0
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
            font = pygame.font.Font(None,20)  #폰트 설정 : none(기본폰트), 30(폰트크기)
            text1 = font.render("Time step :",True,(10,10,10))  #텍스트가 표시된 Surface 를 만듬
            text2 = font.render("Mode : run",True,(10,10,10))
            text3 = font.render(str(count),True,(10,10,10))
            screen.blit(text1,(810,20))
            screen.blit(text3,(883,20))  
            screen.blit(text2,(810,40))
            count+=1       

            pygame.display.update()

        elif not running:
            update(screen, cells, 8)
            font = pygame.font.Font(None,20)  #폰트 설정 : none(기본폰트), 30(폰트크기)
            text1 = font.render("Time step : 0",True,(10,10,10))  #텍스트가 표시된 Surface 를 만듬
            text2 = font.render("Mode : edit",True,(10,10,10))
            screen.blit(text1,(810,20))  
            screen.blit(text2,(810,40))
            count=0 

            pygame.display.update()

        time.sleep(0.01)

if __name__ == '__main__':
    main()