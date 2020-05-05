import pygame
from pygame.locals import *
from pygame import gfxdraw
import math
import random
import time


pygame.init()
window = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Projectile Simulation")
def setBackGround(window):
    window.fill((135, 206, 235),(0,0,window.get_width(),window.get_height()*(4/5)))
    window.fill((34, 139, 34),(0,window.get_height()*(4/5),window.get_width(),window.get_height()))
    #(34, 139, 34)
    #(124, 252, 0)

def getStartPos(window,angle):
    barrel_length = 50
    # angle = angle*(math.pi/180)
    wheelCenter = (50,int(window.get_height()*(4/5))+5)
    end_x = wheelCenter[0] + barrel_length*math.cos(angle)
    end_y = wheelCenter[1] - barrel_length*math.sin(angle)
    return (end_x,end_y)

def drawCannon(window,angle):
    barrel_length = 50
    # angle = angle*(math.pi/180)
    wheelCenter = (50,int(window.get_height()*(4/5))+5)
    end_x = wheelCenter[0] + barrel_length*math.cos(angle)
    end_y = wheelCenter[1] - barrel_length*math.sin(angle)
    pygame.draw.line(window,(80, 80, 80),wheelCenter,(end_x,end_y),5)
    pygame.draw.circle(window,(112, 128, 144),wheelCenter,15,0)

#initial setup
angle = float(input("Enter the Angle: "))
angle = angle*(math.pi/180)
start_pos = getStartPos(window,angle)

muzzleVelocity = float(input("Enter the muzzleVelocity: "))
sample_time = float(input("Enter the sample_time: "))
gravity = float(input("Enter the gravity: "))
windSpeed = float(input("Enter the Wind Speed: "))
windAcceleration = float(input("Enter the Wind Acceleration: "))
feild_length = float(input("Enter the feild length: "))
path = []
def getinput():
    global muzzleVelocity,sample_time,gravity,windSpeed,windAcceleration,feild_length,path
    muzzleVelocity = float(input("Enter the muzzleVelocity: "))
    sample_time = float(input("Enter the sample_time: "))
    gravity = float(input("Enter the gravity: "))
    windSpeed = float(input("Enter the Wind Speed: "))
    windAcceleration = float(input("Enter the Wind Acceleration: "))
    feild_length = float(input("Enter the feild length: "))
    path = []

#current variables
Hx = 0
Hy = 0
Vx = muzzleVelocity*math.cos(angle)
Vy = muzzleVelocity*math.sin(angle)
currentAngle = angle


# print(Vx,Vy)

def setText(window,angle,currentAngle,Hx,Hy,Vx,Vy,Sec):
    basicfont = pygame.font.SysFont(None,30)

    string1 = "Time = {}sec    Angle = {}°    Hx = {}m    Vx = {}m/s".format(round(Sec,2),round(angle,2),round(Hx,2),round(Vx,2))
    string2 = "currentAngle = {}°     Hy = {}m    Vy = {}m/s".format(round(currentAngle,2),round(Hy,2),round(Vy,2))

    text1 = basicfont.render(string1, True ,(165, 42, 42))
    text1Rect = text1.get_rect()
    text1Rect.centerx = 465
    text1Rect.centery = window.get_height()*(4/5) + 50

    text2 = basicfont.render(string2, True ,(165, 42, 42))
    text2Rect = text2.get_rect()
    text2Rect.centerx = 500
    text2Rect.centery = window.get_height()*(4/5) + 100
    window.blit(text1,text1Rect)
    window.blit(text2,text2Rect)

def updateProjectile():
    global sample_time,windSpeed,windAcceleration,Vx,Vy,Hx,Hy,currentAngle,path

    windSpeed = windSpeed + windAcceleration*sample_time
    Vx = Vx + windSpeed
    Vy = Vy + gravity*sample_time
    Hx = Hx + Vx*sample_time
    Hy = Hy + Vy*sample_time
    path.append((Hx,Hy))
    currentAngle = math.atan(Vy/Vx)

def drawProjectile(window,Hx,Hy):
    global start_pos

    Px = (1000/feild_length)*Hx + start_pos[0]
    Py = start_pos[1] - (1000/feild_length)*Hy

    pygame.draw.circle(window,(0,0,0),(int(Px),int(Py)),5,0)

def finalScreen(window,once):
    if(once==False):
        return
    global path, Hx, Hy, feild_length, start_pos
    if(Hx>start_pos[0]):
        #
        outY = 0
        outX = 0
        maxx =  max(path)[0]
        maxy =  max(path)[1]
        if(maxy*(1000/feild_length) > 600):
            outY = maxy*(1000/feild_length)-600
        if(maxx*(1000/feild_length) > 1000):
            outX = maxx*(1000/feild_length)-1000
        newScale = 1000/feild_length

        print(outX,outY)
        if(outX>outY):
            newScale = (1000)/(maxx*2)
        elif(outY>outX):
            newScale = 1000/(maxy*2)
        print(newScale)
        window.fill((0,0,0))
        setBackGround(window)
        drawCannon(window,angle)
        setText(window,angle,currentAngle,Hx,Hy,Vx,Vy,time.time()-start)
        for i in range(0,len(path)-1):
            Pxi = newScale*path[i][0] + start_pos[0]
            Pyi= start_pos[1] - newScale*path[i][1]
            Pxj = newScale*path[i+1][0] + start_pos[0]
            Pyj = start_pos[1] - newScale*path[i+1][1]

            pygame.draw.line(window,(255,0,0),(Pxi,Pyi),(Pxj,Pyj),1)

        Px = newScale*Hx + start_pos[0]
        Py = start_pos[1] - newScale*Hy
        pygame.draw.circle(window,(0,0,0),(int(Px),int(Py)),5,0)

    else:
        outY = 0
        outX = 0
        minx =  min(path)[0]
        maxy =  max(path)[1]
        if(maxy*(1000/feild_length) > 600):
            outY = maxy*(1000/feild_length)-600
        if(minx*(1000/feild_length) < 0):
            outX = minx*-1 + 100

        newScale = 1000/feild_length
        if(outX>outY):
            newScale = (1000)/(minx*2)
        elif(outY>outX):
            newScale = 1000/(maxy*2)
        start_pos_old = start_pos
        start_pos = (900,start_pos[1])
        setBackGround(window)
        drawCannon(window,angle)
        setText(window,angle,currentAngle,Hx,Hy,Vx,Vy,time.time()-start)
        for i in range(0,len(path)-1):
            Pxi = -newScale*path[i][0] + start_pos[0]
            Pyi= start_pos[1] - newScale*path[i][1]
            Pxj = -newScale*path[i+1][0] + start_pos[0]
            Pyj = start_pos[1] - newScale*path[i+1][1]

            pygame.draw.line(window,(255,0,0),(Pxi,Pyi),(Pxj,Pyj),1)
        barrel_length = 50
        # angle = angle*(math.pi/180)
        wheelCenter = (start_pos[0],start_pos_old[1])
        end_x = wheelCenter[0] + barrel_length*math.cos(angle)
        end_y = wheelCenter[1] - barrel_length*math.sin(angle)
        pygame.draw.line(window,(80, 80, 80),wheelCenter,(end_x,end_y),5)
        pygame.draw.circle(window,(112, 128, 144),(int(wheelCenter[0]),int(wheelCenter[1])),15,0)
running = True
updating = True
once = True
start = time.time()
while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_r):
                getinput()
                update = True
                once = True
    if(updating):
        window.fill((0,0,0))
        setBackGround(window)
        drawCannon(window,angle)
        setText(window,angle,currentAngle,Hx,Hy,Vx,Vy,time.time()-start)
        updateProjectile()
        #start_pos = (Hx,Hy)
        drawProjectile(window,Hx,Hy)
        pygame.display.update()
    if( start_pos[1] - Hy*(1000/feild_length) > window.get_height()*(4/5)):
        updating = False
        finalScreen(window,once)
        once = False
        pygame.display.update()
    time.sleep((1/60)*sample_time)
