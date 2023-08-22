#implement the lifegame animation using pygame

import random
import time
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *
import pygame



pygame.init() #초기화
screen = pygame.display.set_mode((1200,800)) #화면 크기 설정
screen.fill((255,255,255)) #배경 색깔 설정
pygame.display.update() #화면 업데이트
pygame.display.set_caption("lifegame") #게임 이름

#implement the lifegame animation using pygame
#lifegame

running = True #게임이 진행중인가?
while running:


    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님

pygame.quit() #게임 종료