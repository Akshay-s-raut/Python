import socket, time, os, webbrowser
import pyautogui as pag
from music_player import *
from ntp_test import *

serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
# host = '192.168.0.7'
port = 9997
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, port))
serversocket.listen(5)
clientsocket,addr = serversocket.accept()

while True:
	msg = input("Play Video: ")
	if(msg.lower()=='exit'):
		break

	clientsocket.send(msg.encode('ascii'))


	# clientsocket.send('{}'.format(msg).encode('ascii'))
	# diff = get_difference()
	# while (time.time()<t):
	#     pass
	play_video(msg,10)
	# print(t)

clientsocket.close()


# https://www.youtube.com/watch?v=dQw4w9WgXcQ
