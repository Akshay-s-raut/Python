import time, webbrowser, pyautogui as pag, random
from PIL import Image


skipper = 10

def setRGB(t):
    #editColor = Image.open('editColor.PNG')
    #xa,ya = pag.center(pag.locateOnScreen(editColor))
    xa,ya = 1160,88
    pag.click(xa,ya,button='left')
    time.sleep(0.5)
    #red = Image.open('red.PNG')
    #xr,yr = pag.center(pag.locateOnScreen(red))
    xr,yr = 1215,605
    pag.click(xr,yr,button='left',clicks=2)
    pag.typewrite(str(t[0]))
    pag.press('tab')
    pag.typewrite(str(t[1]))
    pag.press('tab')
    pag.typewrite(str(t[2]))
    pag.press('enter')

path = input("Enter path of the Image: ")
precision = int(input("Enter precision: "))
offsetx,offsety = [int(i) for i in input().split()]

time.sleep(5)
print("Starting...")

picture = Image.open(path)
sizes = picture.size
imageDict = {}

i=0
j=0
while(i<sizes[0]):
    j=0
    while(j<sizes[1]):
        colorValue = picture.getpixel((i,j))
        if(colorValue in imageDict):
            imageDict[colorValue].append((i,j))
        else:
            imageDict[colorValue]=[(i,j)]
        j=j+precision
    i=i+precision
for i in imageDict.items():
    setRGB(i[0])
    for j in i[1]:
        pag.click(j[0]+offsetx,j[1]+offsety,button='left')
