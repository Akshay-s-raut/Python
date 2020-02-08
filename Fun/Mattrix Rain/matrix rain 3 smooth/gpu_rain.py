import random
import time
import os
from numba import jit, cuda
f = open(r"D:\Programs\Python programs\Fun\matrix rain 2\unicode_characters.txt",encoding='UTF-8').read()
f = f.split()


class RainDrop:
    color=None
    character=None
    def __str__(self):
        return self.color+"{}\033[0m".format(self.character)
    def toString(self):
        return self.color+"{}\033[0m".format(self.character)


def getrandomUnicode():
    g = RainDrop()
    g.character = random.choice(f)
    return g


def print_in_color(color,text):
    color = color.lower()
    colors = {"black":"30","red":"31","green":"32","yellow":"33","blue":"34","magenta":"35","cyan":"36","white":"37"}
    str = "\033["+colors[color]+"m"+text+"\033[0m"
    print(str)

def probability(skewed=-1):
    if(skewed==-1):
        return random.choice([True,False])
    else:
        skewed = "{}".format(skewed)
        w,x = skewed.split('.')
        deno = len(x)
        x = int(x)
        true_array = [True]*x
        false_array = [False]*(10**deno-x)
        arr = true_array + false_array
        return random.choice(arr)


def getRandomColor():
    colors = {"red":"31","green":"32","yellow":"33","blue":"34","magenta":"35","cyan":"36","white":"37"}
    x,y = random.choice(list(colors.items()))
    str = "\033["+y+"m"
    return str

#v = float(input("Enter intial starting speed: "))
#g = float(input("Enter Gravitational acceleration: "))

def makeFrame(Width,Length,frame):
    if(len(frame)==0):
        s=[]
        for i in range(0,Width):
            if(probability(-1)==True):
                x = getrandomUnicode()
                x.color = getRandomColor()
                s.append(x)
            else:
                s.append(None)
        frame.insert(0,s)
    else:
        s=[]
        for i in range(0,Width):
            if(frame[0][i]!=None):
                p = 0.7
            else:
                p = -1
            if(probability(p)==True):
                if(frame[0][i]!=None):
                    x = getrandomUnicode()
                    x.color = frame[0][i].color
                    s.append(x)
                else:
                    x =  getrandomUnicode()
                    x.color = getRandomColor()
                    s.append(x)
            else:
                s.append(None)
        frame.insert(0,s)
    return frame[:Length]


#clearWindow = lambda: os.system('cls') #on Windows System

@jit
def getFrameAsAString(Frame):
    s=""
    for i in Frame:
        for j in i:
            if(j==None):
                s = s + " "
            else:
                s = s + j.toString()
        s = s + "\n"
    return s

@jit
def main(Width,Lenght,fps):
    os.system('cls')
    frame=[]
    #frame2 = makeFrame(Width,Lenght,frame)
    #print(getFrameAsAString(frame2))
    #print(frame)
    while(True):
        frame2 = makeFrame(Width,Lenght,frame)
        print(getFrameAsAString(frame2))
        frame = frame2
        time.sleep(1/fps)
        os.system('cls')

if __name__=="__main__":
    Width = int(input("Enter Width: "))
    Length = int(input("Enter Length: "))
    fps = int(input("Enter FPS: "))
    main(Width,Length,fps)
