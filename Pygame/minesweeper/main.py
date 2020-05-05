import numpy as np
import random
import pygame
from pygame.locals import *
import time
import math
pygame.init()

x,y = [int(i) for i in input("Enter the dimensions: ").split()]
mines = int(input("Enter number of mines: "))
width = 50
height = 50

feild = [[0 for i in range(0,x)] for i in range(0,y)]
minescount=0
revealed = [[False for i in range(0,x)] for i in range(0,y)]
flagged = [[False for i in range(0,x)] for i in range(0,y)]
# revealed[5][5]=True
# revealed[5][6]=True


if(mines>x*y):
    print("Number of Mines should me less than {}".format(x*y))
else:
    while(minescount<mines):
        tempx = random.randrange(0,x)
        tempy = random.randrange(0,y)
        if(feild[tempy][tempx]!='X'):
            minescount = minescount+1
            feild[tempy][tempx]='X'

for i in range(0,y):
    for j in range(0,x):
        if(feild[i][j]!='X'):
            count = 0
            if(j>0 and i>0 and feild[i-1][j-1]=='X'):
                count = count + 1
            if(i>0 and feild[i-1][j]=='X'):
                count = count + 1
            if(i>0 and j<x-1 and feild[i-1][j+1]=='X'):
                count = count + 1
            if(j<x-1 and feild[i][j+1]=='X'):
                count = count + 1
            if(i<y-1 and j<x-1 and feild[i+1][j+1]=='X'):
                count = count + 1
            if(i<y-1 and feild[i+1][j]=='X'):
                count = count + 1
            if(i<y-1 and j>0 and feild[i+1][j-1]=='X'):
                count = count + 1
            if(j>0 and feild[i][j-1]=='X'):
                count = count + 1
            feild[i][j] = count
sizex = (x+1)*width
sizey = (y+1)*height
if((x+1)*50<500):
    sizex = 500
if((y+1)*50<400):
    sizey = 400
window = pygame.display.set_mode((sizex,sizey),0,32)
# window = pygame.display.set_mode(((x+1)*width,(y+1)*height),0,32)
pygame.display.set_caption("minesweeper")

def getCoordinate(x,y,width,height):
    return (x*width, y*height)

def getBox(x,y,xglob,yglob,width,height,window):
    wx = window.get_rect().centerx
    wy = window.get_rect().centery
    if(xglob%2==0):
        tempx = wx - (xglob/2)*width
    else:
        tempx = wx - (xglob//2)*width - width/2
    if(yglob%2==0):
        tempy = wy - (yglob/2)*height
    else:
        tempy = wy - (yglob//2)*height - height/2
    if((x-tempx)<0 or (y-tempy)<0):
        return None
    if( (x-tempx)//width >= xglob or  (y-tempy)//height >= yglob):
        return None
    print(((x-tempx)//width,(y-tempy)//height))
    return (int((x-tempx)//width),int((y-tempy)//height))

# 139 148 148
def makeGrid(x,y,feildreal,revealed,window,width,height,flagged):
    window.fill((255,255,255))
    color = (139,148,148)

    feild = pygame.Surface((x*width,y*height))
    feildRect = feild.get_rect()
    feildRect.centerx = window.get_rect().centerx
    feildRect.centery = window.get_rect().centery
    start = feildRect.topleft
    start = (start[0]+width/2,start[1]+height/2)

    for i in range(0,y):
        for j in range(0,x):
            if(revealed[i][j]==False and flagged[i][j]==True):
                image = pygame.image.load(r'D:\Programs\Python programs\Pygame\minesweeper\box2.PNG')
                flag = pygame.image.load(r'D:\Programs\Python programs\Pygame\minesweeper\flag2.PNG')
                flagRect = flag.get_rect()
                flagRect.centerx = image.get_rect().centerx
                flagRect.centery = image.get_rect().centery
                image.blit(flag,flagRect)
            elif(revealed[i][j]==True):
                image = pygame.image.load(r'D:\Programs\Python programs\Pygame\minesweeper\box4.PNG')
                basicfont = pygame.font.SysFont(None,48)
                if(feildreal[i][j] == 0):
                    text = basicfont.render("", True,(0,0,255))
                elif(feildreal[i][j]==1):
                    text = basicfont.render(str(feildreal[i][j]), True,(0,0,255))
                elif(feildreal[i][j]==2):
                    text = basicfont.render(str(feildreal[i][j]), True,(51,166,56))
                else:
                    text = basicfont.render(str(feildreal[i][j]), True,(255,0,0))
                textRect = text.get_rect()
                textRect.centerx = image.get_rect().centerx
                textRect.centery = image.get_rect().centery
                image.blit(text,textRect)
            else:
                image = pygame.image.load(r'D:\Programs\Python programs\Pygame\minesweeper\box2.PNG')
            feild.blit(image,getCoordinate(j,i,width,height))
    return [feild,feildRect]

temp = makeGrid(x,y,feild,revealed,window,width,height,flagged)
window.blit(temp[0],temp[1])
pygame.display.update()
gamerun = True
firstclick = True
moves = 0
while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()

        elif(event.type == pygame.MOUSEBUTTONDOWN and gamerun==True):
            # if the left button is pressed
            if event.button == 1:
                if(firstclick==True):
                    start = time.time()
                    for i in range(0,y):
                        for j in range(0,x):
                            if(feild[i][j]==0):
                                if(j>0 and i>0 and feild[i-1][j-1]!='X'):
                                    revealed[i-1][j-1] = True
                                if(i>0 and feild[i-1][j]!='X'):
                                    revealed[i-1][j] = True
                                if(i>0 and j<x-1 and feild[i-1][j+1]!='X'):
                                    revealed[i-1][j+1] = True
                                if(j<x-1 and feild[i][j+1]!='X'):
                                    revealed[i][j+1] = True
                                if(i<y-1 and j<x-1 and feild[i+1][j+1]!='X'):
                                    revealed[i+1][j+1] = True
                                if(i<y-1 and feild[i+1][j]!='X'):
                                    revealed[i+1][j] = True
                                if(i<y-1 and j>0 and feild[i+1][j-1]!='X'):
                                    revealed[i+1][j-1] = True
                                if(j>0 and feild[i][j-1]!='X'):
                                    revealed[i][j-1] = True
                                revealed[i][j]=True
                    firstclick=False
                pos = event.pos
                print(pos,'left')
                t = getBox(pos[0],pos[1],x,y,width,height,window)
                if(t!=None):
                    i,j = t
                    revealed[j][i] = True
                temp = makeGrid(x,y,feild,revealed,window,width,height,flagged)
                window.blit(temp[0],temp[1])
                pygame.display.update()

                if(t!=None and feild[j][i]=='X'):
                    gameover = pygame.image.load(r'D:\Programs\Python programs\Pygame\minesweeper\gameover2.PNG')
                    gameoverRect = gameover.get_rect()
                    gameoverRect.centerx = window.get_rect().centerx
                    gameoverRect.centery = window.get_rect().centery
                    window.blit(gameover,gameoverRect)
                    pygame.display.update()
                    gamerun = False
                moves = 0
                for i in revealed:
                    for j in i:
                        if(j==True):
                            moves = moves + 1
                if(moves == x*y-mines and gamerun==True):
                    basicfont = pygame.font.SysFont(None,48)
                    text = basicfont.render("You Won!", True,(0,0,0))
                    textRect = text.get_rect()
                    textRect.centerx = window.get_rect().centerx
                    textRect.centery = window.get_rect().centery-15
                    window.blit(text,textRect)

                    text2 = basicfont.render("in {} seconds".format(int(time.time()-start)), True,(0,0,0))
                    text2Rect = text2.get_rect()
                    text2Rect.centerx = window.get_rect().centerx
                    text2Rect.centery = window.get_rect().centery+15
                    window.blit(text2,text2Rect)

                    pygame.display.update()
            # if the right button is pressed
            elif event.button == 3:
                pos = event.pos
                print(pos,'right')
                t = getBox(pos[0],pos[1],x,y,width,height,window)
                if(t!=None):
                    i,j = t
                    if(flagged[j][i]==True):
                        flagged[j][i]=False
                    else:
                        flagged[j][i]=True
                    temp = makeGrid(x,y,feild,revealed,window,width,height,flagged)
                    window.blit(temp[0],temp[1])
                    pygame.display.update()
