print('Lagranges interpolation for unequal intervals')
n=int(input('enter the size of data: '))
x=list()
y=list()
for i in range(0,n):
    valx=float(input())
    valy=float(input())
    x.append(valx)
    y.append(valy)
interpolX=float(input('Enter the value of X at which u wish to calculate Y: '))
finalTerms=list()
x2=list()
for i in range(0,n):
    x2=x.copy()
    temp=x[i]
    x2.remove(x[i])
    interpolatedY=1
    for j in range(0,n-1):
        interpolatedY=interpolatedY*((interpolX-x2[j])/(temp-x2[j]))
    finalTerms.append(interpolatedY*y[i])
print('The value of Y at given X=',interpolX,'is',sum(finalTerms))
