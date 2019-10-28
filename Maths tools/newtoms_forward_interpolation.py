print('Newtons forward interpolation program')
n=int(input('Enter the number of observations: '))
x=list()
y=list()
print('Enter the values for X: ')
for i in range(0,n):
    varx=float(input())

    x.append(varx)
print('Enter the values for Y:  ')
for i in range(0,n):
    vary=float(input())
    y.append(vary)

interpolX=float(input('Enter the value of x at which u wish to calculate Y: '))
def ncr(n,r):#definig ncr function
    numerator=1
    denominator1=1
    denominator2=1
    for i in range(1,n+1):
        numerator=numerator*i
    for i in range(1,r+1):#to calculate r!
            denominator1=denominator1*i
    for i in range(1,(n-r+1)):#to calculate (n-r)!
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
p=(interpolX-x[0])/(x[1]-x[0])
interpolatedY=y[0]
deno=1
l=1
for i in range(0,n-1):
    deno=deno*(i+1)
    l=l*(p-i)
    interpolatedY= interpolatedY+((l)/deno)*deltaY[i]
print('The value of Y at given x=',interpolX,' is equal to',interpolatedY)
