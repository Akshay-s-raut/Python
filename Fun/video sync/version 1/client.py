import socket, time, os, webbrowser
import pyautogui as pag
from music_player import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9996
s.connect((host, port))

while True:
    msg = s.recv(1024)
    x = msg.decode('ascii')
    x = x.split()
    if(x[0].lower()=='exit'):
        break
    else:
        # t = s.recv(1024)
        # t = int(msg.decode('ascii'))
        # print(time.time(),t)
        # while(time.time()<int(x[1])):
            # pass
        print('Playing video: '+x[0])
        play_video(x[0],x[1]+10)
s.close()
