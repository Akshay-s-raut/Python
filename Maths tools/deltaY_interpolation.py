n=int(input('Enter number of values '))
y=list()
for i in range(0,n):
    s=float(input())
    y.append(s)
def ncr(n,r):
    numerator=1
    denominator1=1
    denominator2=1
    for i in range(1,n+1):
        numerator=numerator*i
    for i in range(1,r+1):
        denominator1=denominator1*i
    for i in range(1,(n-r+1)):
        denominator2=denominator2*i
    value= (numerator)/(denominator1*denominator2)
    return value
deltaY=list()
for t in range(1,n):
    k=0
    for i in range(0,t+1):
            k=k+(ncr(t,i))*y[t-i]*((-1)**i)
    deltaY.append(k)
print(deltaY)
