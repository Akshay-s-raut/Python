n=int(input('Enter the number: '))
ans=list()

while(n!=1):
    if(n%2==0):
        s="{} is Even: {}/2 = {} ".format(n,n,n//2)
        n=n//2
    else:
        s="{} is Odd: 3*{}+1 = {} ".format(n,n,3*n+1)
        n=3*n+1
    ans.append(s)
if(ans[-1][-1]=='1'):
    ans.append("Reached 1")

for i in ans:
    print(i)
