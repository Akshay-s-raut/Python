import pygame
from pygame.locals import *
import time

x,y = [int(i) for i in input("Enter size of the grid: ").split()]
pygame.init()
window = pygame.display.set_mode(((x+1)*50,(y+1)*50),0,32)
pygame.display.set_caption("minesweeper")

def getCoordinate(x,y,width,height):
    return (x*width, y*height)

# 139 148 148
def makeGrid(x,y,window):
    width = 50
    height = 50
    color = (139,148,148)

    image = pygame.image.load(r'D:\Programs\Python programs\Pygame\minesweeper\box2.PNG')

    feild = pygame.Surface((x*width,y*height))
    feildRect = feild.get_rect()
    feildRect.centerx = window.get_rect().centerx
    feildRect.centery = window.get_rect().centery
    start = feildRect.topleft
    start = (start[0]+width/2,start[1]+height/2)

    for i in range(0,y):
        for j in range(0,x):
            feild.blit(image,getCoordinate(j,i,width,height))
            # t = getCoordinate(i,j,width,height)
            # box = pygame.Rect(t[0],t[1],width,height)
            # pygame.draw.rect(feild,color,box)
    return [feild,feildRect]

temp = makeGrid(x,y,window)
window.blit(temp[0],temp[1])
pygame.display.update()
while True:
    for i in pygame.event.get():
        if(i.type == pygame.QUIT):
            pygame.quit()
