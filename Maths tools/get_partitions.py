print("Ferrers Diagram for all Partitions of N")
part=list()
partsi=list()
#try to memoize the recurrence for efficiency
def getPartitions(n,max):
    sum = 0
    if n==0:
        partj=partsi.copy()
        part.append(partj)
        del partsi[-1]
        return 1
    elif n<0:
        del partsi[:]
        return 0
    else:
        for i in range(1,n+1):
            if(i<=max):
                partsi.append(i)
                sum = sum + getPartitions(n-i,i)
        try:
            del partsi[-1]
            return sum
        except:
            return sum
N = int(input("Enter the Number N: "))
print()
getPartitions(N,N+1)

def ferrers_diagram(a):
    s=''
    for i in a:
        s = s + '.'*i + '\n'
    return s.lstrip()

for i in part:
    s = ''
    for j in i:
        s = s + ' {}'.format(j)
    print(s.lstrip())
    print(ferrers_diagram(i))
print("Number of parts = ",len(part))
print()
print(part)
