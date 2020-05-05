import numpy as np
import random
x,y = 10,10
mines = 10

feild = [[0 for i in range(0,x)] for i in range(0,y)]

minescount=0
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
print(np.array(feild))
