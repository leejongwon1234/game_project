#lifegame

import random
import time
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *

def init():
    global outlife
    outlife = np.zeros((102,102),dtype=int)
    life = np.zeros((100,100),dtype=int)
    for i in range(100):
        for j in range(100):
            life[i,j] = random.randint(0,1)

    #outlife + life
    for i in range(100):
        for j in range(100):
            outlife[i+1,j+1] = life[i,j]



#draw life
def draw():
    global outlife
    drawlife = np.zeros((102,102),dtype=int)
    for i in range(102):
        for j in range(102):
            if outlife[i,j] == 1:
                drawlife[i,j] = 0
            else:
                drawlife[i,j] = 1
    plt.imshow(drawlife , cmap='gray', interpolation='nearest')

#update life
def update():
    global outlife
    newlife = np.zeros((102,102))
    for i in range(100):
        for j in range(100):
            total = (outlife[(i+1),j] + outlife[(i+1),(j+2)] + outlife[(i),(j+1)] + outlife[(i+2),(j+1)] + outlife[(i),(j)] + outlife[(i),(j+2)] + outlife[(i+2),(j)] + outlife[(i+2),(j+2)])
            if outlife[i+1,j+1] == 1:
                if (total == 2) or (total == 3):
                    newlife[i+1,j+1] = 1
                else:
                    newlife[i+1,j+1] = 0
            else:
                if total == 3:
                    newlife[i+1,j+1] = 1
                else:
                    newlife[i+1,j+1] = 0
    outlife = newlife


#main
init()
while True:
    
    drawnow(draw)
    time.sleep(0.001)
    comparison_life = outlife
    time.sleep(0.001)
    update()
    time.sleep(0.001)
    #comparison_life == outlife 이면 break
    if (comparison_life == outlife).all():
        break
    time.sleep(0.001)
    
