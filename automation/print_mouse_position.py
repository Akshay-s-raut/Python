import pyautogui as pag
import time
from matplotlib import pyplot as plt

t = int(input("Enter time duration: "))
k = float(input("Enter the Sampling rate: "))

x = []
y = []
time.sleep(10)
print("Start Now!")
start_time = time.time()

while(time.time() < start_time + t):
    xi,yi = pag.position()
    x.append(xi)
    y.append(1079-yi)
    time.sleep(k)


print("Ploting...")
plt.plot(x,y,color='red',label='Coustom function')
plt.show()
