import time, webbrowser, pyautogui as pag, random
from PIL import Image

N = int(input('Enter the Number of Messages: '))
t = float(input("Enter duration: "))

#webbrowser.open("https://web.whatsapp.com/")
time.sleep(10)
print("Starting...")
im = Image.open("texting_bar.PNG")
x,y = pag.center(pag.locateOnScreen(im))
pag.click(x,y,button='left')

filter = open("D:\Programs\PYTHON programs\Fun\dictionary_194,000_words.txt").read()
filter = filter.split()

for i in range(0,N):
    pag.typewrite(random.choice(filter))
    #pag.typewrite("I Love U !❤")
    pag.press('enter')
    time.sleep(t)
