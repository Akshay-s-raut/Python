import time

def clearWindow(Widht,Length):
    print("\033[0;0H\033[2K")
    for i in range(0,Length):
        print("\033[2K")
    print("\033[0;0H")
Length=10
Width = 100
for i in range(0,Length):
    for j in range(0,Width):
        print("X",end="")
    print()
time.sleep(2)
clearWindow(Width,Length)
print("hey")
