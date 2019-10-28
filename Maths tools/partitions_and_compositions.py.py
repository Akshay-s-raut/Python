import sys
sys.setrecursionlimit(10**6)

#Number of compositions
CompDict = dict()
def NumberOfCompositions(n):
    sum = 0
    if n==0:
        return 1
    elif n<0:
        return 0
    elif n in CompDict:
        return CompDict[n]
    else:
        for i in range(1,n+1):
            sum = sum + NumberOfCompositions(n-i)
        CompDict[n] = sum
        return sum

#Number of Partitions
parts=dict()
def NumberOfPartitions(n,max):
    sum = 0
    if n==0:
        return 1
    if n<0:
        return 0
    elif (n,max) in parts:
        return parts[(n,max)]
    else:
        for i in range(1,n+1):
            if(i<=max):
                sum = sum + NumberOfPartitions(n-i,i)
        parts[(n,max)]=sum
        return sum


N = int(input("Enter the Number N: "))
print("Number of Compositions of",N,"=",NumberOfCompositions(N))
print("Number of Partitions of",N,"=",NumberOfPartitions(N,N+1))
