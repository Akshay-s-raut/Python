print('All combination generator')
a=input('Enter the array: ')
a=a.split()

def combinations(a):                       # Kind of a DFS
    all_combinations=list()
    if(len(a)==1):
        return a
    else:
        for i in range(0,len(a)):
            for j in combinations(a[:i]+a[i+1:]):
                s = a[i] + j
                all_combinations.append(s)
    return all_combinations

ans=combinations(a)
print(ans)
print('Number of Combinations = {}'.format(len(ans)))
