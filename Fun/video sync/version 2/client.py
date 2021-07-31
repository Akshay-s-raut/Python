import socket, time, os, webbrowser
import pyautogui as pag
from music_player import *
from ntp_test import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9997
s.connect((host, port))

while True:
    msg = s.recv(1024)
    # diff = get_difference()
    x = msg.decode('ascii')
    # x = x.split()
    if(x.lower()=='exit'):
        break
    else:
        print('Playing video: '+x)
        play_video(x,15)
s.close()
