import threading,time
l = []
def A():
    i=0
    while(True):
        l.append(i)
        i = i + 1
def B():
    for i in l:
        print(i)

t1 = threading.Thread(target=A)
t2 = threading.Thread(target=B)

t1.start()
time.sleep(3)
t2.start()
