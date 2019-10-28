import time, webbrowser, pyautogui as pag, random
from PIL import Image

N = int(input("Enter n: "))
T = float(input("Enter duration: "))
path = input("Enter image path:")
time.sleep(10)
print("Starting...")

for i in range(0,N):
    attachment = Image.open("attachment.PNG")
    xa,ya = pag.center(pag.locateOnScreen(attachment))
    pag.click(xa,ya,button='left')
    time.sleep(1)

    pag.moveRel(0,94)
    pag.click()
    time.sleep(1)

    pag.typewrite(path)
    pag.press('enter')
    time.sleep(1)
    pag.press('enter')

    time.sleep(T)
