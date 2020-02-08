from numba import jit, cuda
import os
import time

def f():
    for i in range(0,1000):
        print(i,end="")
    time.sleep(3)

for i in range(0,10):
    os.system('cls')
    f()
