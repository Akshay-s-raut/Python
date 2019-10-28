from math import ceil
from math import log2

def print_tree(a):
    s=len(a)
    height=ceil(log2(s+1))
    last_level=2**(height-1)
    k=int((2*last_level-1)/2)
    tstart=0
    tend=1
    c=0
    l=2
    while(c<len(a)):
        for i in range(0,k):
            print(' ',end='')
        for j in range(tstart,tend):
            if(j<len(a)):
                print(a[j],end='')
            for m in range(0,2*k+1):
                print(' ',end='')
            c=c+1
        tstart=tend
        tend=2**(l)-1
        last_level=last_level//2
        k=int((2*last_level-1)/2)
        l=l+1
        print()
    print()
