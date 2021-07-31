import os, time, webbrowser
import pyautogui as pag
import time
import ntplib
from ntp_test import *

def play_video(url,wait):
    # os.system("pkill "+'firefox')
    # os.system("taskkill /im chrome.exe /f")
    # time.sleep(1)
    diff = get_difference()
    start = time.time()+wait+diff
    webbrowser.open(url, new=2)
    # time.sleep(10)
    while(time.time()<start):
        pass
    pag.press('space')
    print('pressed',time.time(),time.time()+diff+wait)

# play_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
