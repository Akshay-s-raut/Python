n=int(input('Eneter the number of varriables:\n'))
c=list()
constant=list()
print('Enter the values now:')
for i in range(0,n):
    temp=list()
    for j in range(0,n):
        t=float(input())
        temp.append(t)
    c.append(temp)
    cons=float(input('Enter the constant: '))
    constant.append(cons)
print(c)
varriable=list()
for i in range(0,n):
    varriable.append(int(0))
number=list()
for i in range(0,n):
    number.append(int(i))
for m in range(0,50):
    k=0
    s=list()
    nt=list()
    for i in c:
        s=i.copy()
        s.remove(i[k])
        varriable[k]=constant[k]
        nt=number.copy()
        nt.remove(nt[k])
        g=0
        for l in s:
            varriable[k]=varriable[k]-l*varriable[nt[g]]
            g=g+1
        varriable[k]=varriable[k]/i[k]
        k=k+1
    print(varriable)
