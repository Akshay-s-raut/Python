import random
import time
import os
f = open(r"D:\Programs\Python programs\Fun\matrix rain 2\unicode_characters.txt",encoding='UTF-8').read()
f = f.split()

def getrandomUnicode():
    return random.choice(f)

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

Width = int(input("Enter Width: "))
Length = int(input("Enter Length: "))
fps = int(input("Enter FPS: "))
#v = float(input("Enter intial starting speed: "))
#g = float(input("Enter Gravitational acceleration: "))


def makeFrame(Width,Length,frame):
    if(len(frame)==0):
        s=""
        for i in range(0,Width):
            if(probability(0.05)==True):
                s = s + getrandomUnicode()
            else:
                s = s + " "
        frame.insert(0,s)
    else:
        s=""
        for i in range(0,Width):
            if(frame[0][i]!=" "):
                p = 0.7
            else:
                p = 0.05
            if(probability(p)==True):
                s = s + getrandomUnicode()
            else:
                s = s + " "
        frame.insert(0,s)
    return frame[:Length]


#clearWindow = lambda: os.system('cls') #on Windows System

def getFrameAsAString(Frame):
    s=""
    for i in Frame:
        s = s + "\n" + i
    return s[1:]

def main(Width,Lenght):
    os.system('cls')
    frame=[]
    while(True):
        frame2 = makeFrame(Width,Lenght,frame)
        print_in_color("green",getFrameAsAString(frame2))
        frame = frame2
        time.sleep(1/fps)
        os.system('cls')

main(Width,Length)

'''for i in range(0,10):
    makeFrame(Width)
    for j in frame:
        print(j)
    print()'''
