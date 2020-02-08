import time, webbrowser, pyautogui as pag, random
from PIL import Image

offsetx,offsety = 500,500
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

time.sleep(5)
print("Starting...")

picture = Image.open(path)
sizes = picture.size
# print(picture.getpixel((5,5)))
i=0
j=0
while(i<sizes[0]):
    j=0
    while(j<sizes[1]):
        colorValue = picture.getpixel((i,j))
        print(i,j,colorValue)
        setRGB(colorValue)
        #time.sleep(0.2)
        pag.click(i+offsetx,j+offsety,button='left',duration=0.1)
        j = j + skipper
    i = i + skipper
