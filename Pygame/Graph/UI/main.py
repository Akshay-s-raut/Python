import numpy as np
import random
import pygame
from pygame import gfxdraw
from pygame.locals import *
import time
import math
pygame.init()

from graph import *
g = graph(0)


radius = 20
w,h = 1000,600
window = pygame.display.set_mode((w,h),0,32)
pygame.display.set_caption("Graph Editor")

Nodes = {}
edges = []


def isCollsion(t1,t2):
    global radius
    if(((t1[0]-t2[0])**2 + (t1[1]-t2[1])**2)**0.5 < radius):
        return True
    else:
        return False

def drawScreen():
    global window,w,h
    gap = 40
    lineColor = (154,149,251)
    pygame.draw.polygon(window,(101,250,116),((w,0),(w-80,0),(w-80,80),(w,80)))
    for i in range(0,w//gap):
        pygame.draw.line(window,lineColor,(i*gap,0),(i*gap,h),1)
    for i in range(0,h//gap):
        pygame.draw.line(window,lineColor,(0,i*gap),(w,i*gap),1)


def drawNode(value,position,color=(193,172,251)):
    global window,radius
    pygame.gfxdraw.filled_circle(window,position[0],position[1],radius,color)
    basicfont = pygame.font.SysFont(None,25)
    text = basicfont.render(str(value), True ,(0, 0, 255))
    textRect = text.get_rect()
    textRect.centerx = position[0]
    textRect.centery = position[1]
    window.blit(text,textRect)

def drawEdges(color=(255,0,0)):
    global g, window, Nodes, show_weights
    for i in range(0,g.size):
        for j in range(0,g.size):
            if(g.g[i][j]!=0):
                pygame.draw.line(window,color,Nodes[i],Nodes[j],1)
                if(show_weights):
                    basicfont = pygame.font.SysFont(None,30)
                    text = basicfont.render(str(g.g[i][j]), True ,(42, 42, 42))
                    textRect = text.get_rect()
                    textRect.centerx = (Nodes[i][0]+Nodes[j][0])/2
                    textRect.centery = (Nodes[i][1]+Nodes[j][1])/2
                    window.blit(text,textRect)


def drawNodes():
    global window, g
    for i in range(0,g.size):
        drawNode(i,Nodes[i])

def drawOptions():
    global window, w, h
    startx,starty = 10,100
    height = 30
    width = 100
    options = ['Reset','BFS','DFS','Cycle','Kruskal','Prim','Dijkstra']
    for i in range(0,len(options)):
        pygame.draw.polygon(window,(201,176,1),((startx,starty),(startx+width,starty),(startx+width,starty+height),(startx,starty+height)))
        basicfont = pygame.font.SysFont(None,25)
        text = basicfont.render(options[i], True ,(55, 90, 96))
        textRect = text.get_rect()
        textRect.centerx = startx + width/2
        textRect.centery = starty + height/2
        window.blit(text,textRect)
        starty = starty + 60

def getOption(t):
    option = -1
    startx,starty = 10,100
    height = 30
    width = 100
    for i in range(0,7):
        if(t[0]>startx and t[0]<startx+width and t[1]>starty and t[1]<starty+height):
            return i
        starty = starty + 60
    return -1

running = True
dragL = False
objectL = None

dragR = False
EdgeR = None
objectR = None

dragM = False
EdgeM = None
objectM = None

show_weights = False
timeInterval = 0.5
Reset = True
while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

        if(event.type == pygame.MOUSEBUTTONDOWN):


            if(event.button == 1):
                #check for options
                #option menu
                if(getOption(event.pos)!=-1):
                    option = getOption(event.pos)
                    print(option)

                    if(option==0):
                        Reset = True
                        window.fill((255,255,255))
                        drawScreen()
                        drawEdges()
                        drawNodes()
                        drawOptions()
                    elif(option==1):
                        Reset = False
                        chosen = None
                        while(True):
                            if(chosen!=None or g.size==0):
                                break
                            startx,starty = 10,10
                            width = 100
                            height = 30
                            basicfont = pygame.font.SysFont(None,25)
                            text = basicfont.render("Select Source", True ,(0, 255, 0))
                            textRect = text.get_rect()
                            textRect.centerx = startx + width/2
                            textRect.centery = starty + height/2
                            window.blit(text,textRect)
                            pygame.display.update()
                            for event2 in pygame.event.get():
                                if(event2.type == pygame.MOUSEBUTTONDOWN and event2.button==1):
                                    for i,j in Nodes.items():
                                        if(isCollsion(j,event2.pos)):
                                            chosen = i
                                            break
                        if(g.size>0 and chosen!=None):
                            temp = g.BFS(chosen)
                            for i in temp:
                                drawNode(i,Nodes[i],(255,0,0))
                                pygame.display.update()
                                time.sleep(timeInterval)
                            print(temp)

                    elif(option==2):
                        Reset = False
                        chosen = None
                        while(True):
                            if(chosen!=None or g.size==0):
                                break
                            startx,starty = 10,10
                            width = 100
                            height = 30
                            basicfont = pygame.font.SysFont(None,25)
                            text = basicfont.render("Select Source", True ,(0, 255, 0))
                            textRect = text.get_rect()
                            textRect.centerx = startx + width/2
                            textRect.centery = starty + height/2
                            window.blit(text,textRect)
                            pygame.display.update()
                            for event2 in pygame.event.get():
                                if(event2.type == pygame.MOUSEBUTTONDOWN and event2.button==1):
                                    for i,j in Nodes.items():
                                        if(isCollsion(j,event2.pos)):
                                            chosen = i
                                            break
                        if(g.size>0 and chosen!=None):
                            temp = g.DFS(chosen)
                            for i in temp:
                                drawNode(i,Nodes[i],(255,0,0))
                                pygame.display.update()
                                time.sleep(timeInterval)
                            print(temp)
                    elif(option==3):
                        print(3)
                    elif(option==4):
                        Reset = False
                        print(4)
                        temp = g.kruskal()
                        for i,j in temp:
                            pygame.draw.line(window,(0,255,0),Nodes[i],Nodes[j],4)
                            drawNode(i,Nodes[i],(255,0,0))
                            drawNode(j,Nodes[j],(255,0,0))
                            pygame.display.update()
                            time.sleep(timeInterval)
                        print(temp)
                    elif(option==5):
                        Reset = False
                        chosen = None
                        while(True):
                            if(chosen!=None or g.size==0):
                                break
                            startx,starty = 10,10
                            width = 100
                            height = 30
                            basicfont = pygame.font.SysFont(None,25)
                            text = basicfont.render("Select Source", True ,(0, 255, 0))
                            textRect = text.get_rect()
                            textRect.centerx = startx + width/2
                            textRect.centery = starty + height/2
                            window.blit(text,textRect)
                            pygame.display.update()
                            for event2 in pygame.event.get():
                                if(event2.type == pygame.MOUSEBUTTONDOWN and event2.button==1):
                                    for i,j in Nodes.items():
                                        if(isCollsion(j,event2.pos)):
                                            chosen = i
                                            break
                        if(g.size>0 and chosen!=None):
                            temp = g.prim(chosen)
                            for i,j in temp:
                                pygame.draw.line(window,(0,255,0),Nodes[i],Nodes[j],4)
                                drawNode(i,Nodes[i],(255,0,0))
                                drawNode(j,Nodes[j],(255,0,0))
                                pygame.display.update()
                                time.sleep(timeInterval)
                            print(temp)
                    elif(option==6):
                        Reset = False
                        chosen1,chosen2 = None,None
                        while(True):
                            if((chosen1!=None and chosen2!=None) or g.size==0):
                                break
                            startx,starty = 30,10
                            width = 200
                            height = 30
                            basicfont = pygame.font.SysFont(None,25)
                            text = basicfont.render("Select Source and Destination", True ,(0, 255, 0))
                            textRect = text.get_rect()
                            textRect.centerx = startx + width/2
                            textRect.centery = starty + height/2
                            window.blit(text,textRect)
                            pygame.display.update()
                            for event2 in pygame.event.get():
                                if(event2.type == pygame.MOUSEBUTTONDOWN and event2.button==1):
                                    for i,j in Nodes.items():
                                        if(isCollsion(j,event2.pos)):
                                            if(chosen1==None):
                                                chosen1 = i
                                                break
                                            else:
                                                chosen2 = i
                                                break
                        if(chosen1!=None and chosen2!=None and g.size>0):
                            temp = g.dijkstra(chosen1,chosen2)
                            if(temp[0]!=infinity):
                                for i in range(0,len(temp[1])-1):
                                    pygame.draw.line(window,(0,255,0),Nodes[temp[1][i]],Nodes[temp[1][i+1]],4)
                                    drawNode(temp[1][i],Nodes[temp[1][i]],(255,0,0))
                                    drawNode(temp[1][i+1],Nodes[temp[1][i+1]],(255,0,0))
                                    pygame.display.update()
                                    time.sleep(timeInterval)
                                print(temp)

                if(dragL==False):
                    x , y =  event.pos
                    ox, oy = None,None
                    dragL = True
                    for i,j in Nodes.items():
                        if(isCollsion(j,(x,y))):
                            objectL = i
                            ox,oy = Nodes[i]
                            break

            if(event.button == 3):
                if(dragR==False):
                    x , y =  event.pos
                    dragR = True
                    EdgeR = event.pos
                    for i,j in Nodes.items():
                        if(isCollsion(j,(x,y))):
                            objectR = i
                            break
            if(event.button == 2):
                if(dragM==False):
                    x , y =  event.pos
                    dragM = True
                    EdgeM = event.pos
                    for i,j in Nodes.items():
                        if(isCollsion(j,(x,y))):
                            objectM = i
                            break

        if(event.type == pygame.MOUSEBUTTONUP):
            dragL = False
            objectL = None

            if(objectR!=None):
                objectR2=None
                x , y =  event.pos
                for i,j in Nodes.items():
                    if(isCollsion(j,(x,y))):
                        objectR2 = i
                        break
            if(dragR==True and objectR!=None and objectR2!=None):
                if(g.g[objectR][objectR2]!=0):
                    tempw = int(input())
                    g.insertEdge(objectR,objectR2,tempw)
                    g.insertEdge(objectR2,objectR,tempw)
                elif(g.g[objectR][objectR2]==0 and objectR!=objectR2):
                    g.insertEdge(objectR,objectR2)
                    g.insertEdge(objectR2,objectR)
            dragR = False
            objectR = None
            EdgeR = None

            if(objectM!=None):
                objectM2 = None
                x , y =  event.pos
                for i,j in Nodes.items():
                    if(isCollsion(j,(x,y))):
                        objectM2 = i
                        break
            if(dragM==True and objectM!=None and objectM2!=None):
                if(objectM!=objectM2):
                    g.insertEdge(objectM,objectM2,0)
                    g.insertEdge(objectM2,objectM,0)
            dragM = False
            objectM = None
            EdgeM = None

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_a):
                Nodes[len(Nodes)]=(w-40,40)
                g.insertNode()

            if(event.key == pygame.K_x):
                for i in range(0,g.size):
                    if(Nodes[i][0]>w-80 and Nodes[i][0]<w and Nodes[i][1]>0 and Nodes[i][1]<80):
                        g.removeNode(i)
                        del Nodes[i]

                        NodesNew = {}
                        start=0
                        for i,j in Nodes.items():
                            NodesNew[start] = j
                            start = start + 1
                        Nodes = NodesNew
                        break
            if(event.key == pygame.K_w):
                if(show_weights==True):
                    show_weights = False
                else:
                    show_weights = True
            if(event.key == pygame.K_g):
                print(Nodes)
                print(g)

    if(objectL!=None and dragL==True):
        if(Nodes[objectL][0]<135):
            Nodes[objectL] = (136 , event.pos[1])
            dragL = False
        else:
            Nodes[objectL] = (event.pos[0],event.pos[1])
    if(objectR!=None and dragR==True):
        pygame.draw.line(window,(255,0,0),Nodes[objectR],EdgeR,1)
    # if(objectM!=None and dragM==True):
    #     pygame.draw.line(window,(255,0,0),Nodes[objectR],EdgeR,1)


    if(Reset):
        window.fill((255,255,255))
        drawScreen()
        drawEdges()
        drawNodes()
        drawOptions()
    pygame.display.update()
