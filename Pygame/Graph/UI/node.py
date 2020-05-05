import numpy as np
import random
import pygame
from pygame import gfxdraw
from pygame.locals import *
import time
import math
pygame.init()

radius = 20
w,h = 500,400
window = pygame.display.set_mode((w,h),0,32)

def drawNode(value,position):
    global window,radius
    pygame.gfxdraw.filled_circle(window,position[0],position[1],radius,(193,172,251))
    basicfont = pygame.font.SysFont(None,25)
    text = basicfont.render(str(value), True ,(0, 0, 255))
    textRect = text.get_rect()
    textRect.centerx = position[0]
    textRect.centery = position[1]
    window.blit(text,textRect)

window.fill((255,255,255))
drawNode(0,(50,100))
pygame.display.update()


running = True
while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
