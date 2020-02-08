import time, webbrowser, pyautogui as pag, random
from PIL import Image
time.sleep(5)

def setRGB(t):
    editColor = Image.open('editColor.PNG')
    xa,ya = pag.center(pag.locateOnScreen(editColor))
    pag.click(xa,ya,button='left')
    time.sleep(0.5)
    red = Image.open('red.PNG')
    xr,yr = pag.center(pag.locateOnScreen(red))
    pag.click(xr+30,yr,button='left',clicks=2)
    pag.typewrite(t[0])

    green = Image.open('green.PNG')
    xg,yg = pag.center(pag.locateOnScreen(green))
    pag.click(xg+30,yg,button='left',clicks=2)
    pag.typewrite(t[1])

    blue = Image.open('blue.PNG')
    xb,yb = pag.center(pag.locateOnScreen(blue))
    pag.click(xb+30,yb,button='left',clicks=2)
    pag.typewrite(t[2])
    pag.press('enter')


setRGB(('77','105','6'))
