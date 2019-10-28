import numpy as np
n=int(input('Enter the number of variables: '))
coefficientsi=list()
constantsi=list()
for i in range(0,n):
    l=list()
    for j in range(0,n):
        x=float(input())
        l.append(x)
    coefficientsi.append(l)
coefficients=np.array(coefficientsi)
print('Enter the constants')
for i in range(0,n):
    x=float(input())
    constantsi.append(x)
constants=np.array(constantsi)
D=list()
for i in range(0,n):
    Dx=coefficients.copy()
    Dx[i]=constants
    D.append(np.linalg.det(Dx))
ans=list()
D0=np.linalg.det(coefficients)
for i in D:
    ans.append(i/D0)
print(ans)
