from math import log2
from math import ceil
def print_tree(a):
    print('Tree')
    last_level = ceil(2**(log2(len(a)+1)))
    elements=2**last_level
    mid=(elements*2-1)//2+1
    i=1
    k=int(T_last_level/8)
    tstart=0
    tend=1
    c=0
    flag=0
    while(c<len(a)):
        for gaps in range(0,k):
            print('\t',end='')
        for j in range(tstart,tend):
            print(a[j],'\t',end='')
            c=c+1
        tstart=tend
        tend=2**(i+1)-1
        if(tend>len(a)-1):
            tend=len(a)
        print()
        print()
        k=k-1
        i=i+1
    print()
print(print_tree([16,4,10,14,7,9,3,2,8,1,2,3,4,5,6]))
