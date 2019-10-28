from math import acos
print('Document distance')
path1=input('Enter Path of document 1: ')
path2=input('Enetr Path of document 2: ')
f1=open(path1).read()
s1=f1.split()
f2=open(path2).read()
s2=f2.split()
counts1=dict()
counts2=dict()
for i in s1:
    counts1[i]=counts1.get(i,0)+1
for i in s2:
    counts2[i]=counts2.get(i,0)+1
sum=0
for i,j in counts1.items():
    for l,m in counts2.items():
        if(i==l):
            sum=sum+j*m
dprime=sum/(len(f1)*len(f2))
d=acos(dprime)
print('Count1 = ',counts1)
print('Count2 = ',counts2)
print('The Documented distance between',path1,'and',path2,'is',d)
