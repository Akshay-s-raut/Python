import os, time, webbrowser
import pyautogui as pag

def play_video(url,t):
    # os.system("pkill "+'firefox')
    # os.system("taskkill /im chrome.exe /f")
    # time.sleep(1)

    webbrowser.open(url, new=2)
    # time.sleep(10)
    while(time.time()<t):
        pass
    pag.press('space')

# play_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
