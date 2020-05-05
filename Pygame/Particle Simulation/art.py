import pygame
from pygame.locals import *
import random
import time
import math

from particle import *

#Constants
N = int(input("Enter Number of Particles = "))
particles = []
radius = 2
rate = 0.1


pygame.init()
winndow_size = (500,400)
window = pygame.display.set_mode(winndow_size,pygame.FULLSCREEN)
# window = pygame.display.set_mode(winndow_size)

def getMagnitude(v):
    return (v[0]**2 + v[1]**2)**0.5

def isCollison(p1,p2,angle1,angle2):
    global radius
    distance = ((p1.Position[0]-p2.Position[0])**2 + (p1.Position[1]-p2.Position[1])**2)**0.5
    if(distance<=2*radius and (getMagnitude(p2.Velocity)*math.cos(angle2) - getMagnitude(p1.Velocity)*math.cos(angle1))<0 ):
        return True
    else:
        return False

def AddParticles(N):
    global particles
    for i in range(0,N):
        p = Particle(getRandomPosition(winndow_size),getRandomVelocity(),getRandomMass(),getRandomColor())
        particles.append(p)

def getAngle(v1,v2):
    if(getMagnitude(v1)==0 or getMagnitude(v2)==0):
        return 0
    x = (v1[0]*v2[0] + v1[1]*v2[1])/(getMagnitude(v1)*getMagnitude(v2))
    if(x>1):
        x = 1
    elif(x<-1):
        x = -1
    return math.acos(x)

def getNewVelocity_1(p1,p2,angle1,angle2):
    return (((p1.Mass-p2.Mass)/(p1.Mass+p2.Mass))*(getMagnitude(p1.Velocity)*math.cos(angle1)) + ((2*p2.Mass)/(p1.Mass+p2.Mass))*(getMagnitude(p2.Velocity)*math.cos(angle2)))

def getNewVelocity_2(p1,p2,angle1,angle2):
    return (((2*p1.Mass)/(p1.Mass+p2.Mass))*(getMagnitude(p1.Velocity)*math.cos(angle1)) - ((p1.Mass-p2.Mass)/(p1.Mass+p2.Mass))*(getMagnitude(p2.Velocity)*math.cos(angle2)))

def updateSandbox(window):
    global particles,rate,radius

    for i in particles:
        if(i.Position[0]<=radius or i.Position[0]>=window.get_width()-radius):
            i.Velocity[0] = -i.Velocity[0]
            if(i.Position[0]<=radius):
                i.Position[0] = radius + 1
            elif(i.Position[0]>=window.get_width()-radius):
                i.Position[0] = window.get_width()-radius-1

        if(i.Position[1]<=radius or i.Position[1]>=window.get_height()-radius):
            i.Velocity[1] = -i.Velocity[1]
            if(i.Position[1]<=radius):
                i.Position[1] = radius + 1
            elif(i.Position[1]>=window.get_height()-radius):
                i.Position[1] = window.get_height()-radius - 1

    for i in range(0,len(particles)):
        for j in range(i+1,len(particles)):
            distance = [particles[j].Position[0]-particles[i].Position[0],particles[j].Position[1]-particles[i].Position[1]]
            angle1 = getAngle(distance,particles[i].Velocity)
            angle2 = getAngle(distance,particles[j].Velocity)
            if(isCollison(particles[i],particles[j],angle1,angle2) and (getMagnitude(particles[i].Velocity)!=0 and getMagnitude(particles[j].Velocity)!=0)):
                if((particles[j].Position[0] - particles[i].Position[0])!=0):
                    theta = math.atan((particles[j].Position[1] - particles[i].Position[1])/(particles[j].Position[0] - particles[i].Position[0]))
                else:
                    theta = math.pi/2
                V1_finalx = getNewVelocity_1(particles[i],particles[j],angle1,angle2)
                V1_finaly = getMagnitude(particles[i].Velocity)*math.sin(angle1)

                V2_finalx = getNewVelocity_2(particles[i],particles[j],angle1,angle2)
                V2_finaly = getMagnitude(particles[j].Velocity)*math.sin(angle2)

                particles[i].Velocity[0] = V1_finalx*math.cos(theta) - V1_finaly*math.sin(theta)
                particles[i].Velocity[1] = V1_finaly*math.cos(theta) + V1_finalx*math.sin(theta)
                particles[j].Velocity[0] = V2_finalx*math.cos(theta) - V2_finaly*math.sin(theta)
                particles[j].Velocity[1] = V2_finaly*math.cos(theta) + V2_finalx*math.sin(theta)

    for i in particles:
        i.updatePosition(rate)
        # i.Velocity[1] = i.Velocity[1] + 9.8*rate

def drawParticles(window):
    global particles,radius

    for i in particles:
        pygame.draw.circle(window,i.Color,i.getPosition(),radius,0)

def displayTotalMomentum():
    global particles,start
    px=0
    py=0
    for i in particles:
        px = px + i.Mass*i.Velocity[0]
        py = py + i.Mass*i.Velocity[1]
    print("Total Momentum at {} = {}".format(round(time.time()-start,2),(round(px,2),round(py,2))))

def displayTotalEnergy():
    global particles,start
    ke = 0
    for i in particles:
        ke = ke + 0.5*(i.Mass)*(getMagnitude(i.Velocity)**2)
    print("Kinetic Energy at {} = {}".format(round(time.time()-start,2),round(ke,2)))

def drawLines(window):
    global particles,N
    for i in range(0,N-1):
        for j in range(i+1,N):
            pygame.draw.line(window,particles[i].Color,particles[i].Position,particles[j].Position,1)
            # pygame.draw.line(window,(0,0,0),particles[i].Position,particles[j].Position,1)
def drawPolygon(window):
    global particles
    verts = []
    for i in particles:
        verts.append(tuple(i.Position))
    pygame.draw.polygon(window,(0,255,0),tuple(verts))
AddParticles(N)
# particles.append(Particle([0,200],[10,0],5,(255,0,0)))
# particles.append(Particle([500,200],[-10,0],5,(0,0,255)))
# print(particles)

running = True
start = time.time()
while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_i):
                displayTotalMomentum()
                displayTotalEnergy()
                print()
    window.fill((0,0,0))
    updateSandbox(window)
    drawParticles(window)
    drawLines(window)
    # drawPolygon(window)
    pygame.display.update()
    # time.sleep(1/30)

# for i in particles:
#     if(i.Position[0]==0 and i.Position[1]!=0):
#         i.Velocity[0] = -i.Velocity[0]
#     elif(i.Position[0]==0 and i.Position[1]==0):
#         i.Velocity[0] = -i.Velocity[0]
#         i.Velocity[1] = -i.Velocity[1]
#     elif(i.Position[0]!=0 and i.Position[1]==0):
