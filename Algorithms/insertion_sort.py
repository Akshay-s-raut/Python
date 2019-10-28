print('Inserion Sort')
n=int(input('Enter the size of the array: '))
rev=int(input('Is Reverse=true? then (Enter -1): '))
a=list()
print('Enter the array:')
for i in range(0,n):
    x=float(input())
    a.append(x)
if(rev==-1):
    for i in range(1,n):
        l=i
        while(a[l]>a[l-1] and l!=0):
            t=a[l]
            a[l]=a[l-1]
            a[l-1]=t
            l=l-1
else:
    for i in range(1,n):
        l=i
        while(a[l]<a[l-1] and l!=0):
            t=a[l]
            a[l]=a[l-1]
            a[l-1]=t
            l=l-1
print(a)
