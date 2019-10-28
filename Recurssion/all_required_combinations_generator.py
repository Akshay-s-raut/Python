print('All required combination generator with no repetitions')
a=input('Enter the array: ')
n=int(input('Enter required length of the combination: '))
a=a.split()

def combinations(a,n):
    all_combinations=list()
    if(len(a)==1):
        return a
    elif(n==1):
        for i in a:
            all_combinations.append(i)
    else:
        for i in range(0,len(a)):
            for j in combinations(a[:i]+a[i+1:],n-1):
                s = a[i] + j
                all_combinations.append(s)

    return all_combinations

ans=combinations(a,n)
print(ans)
print('Number of combinations: {}'.format(len(ans)))
