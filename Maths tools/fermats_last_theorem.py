n = int(input('Enter the power: '))

found=0
start=1
while(found!=1):
    for i in range(1,start):
        for j in range(1,start):
            if(i**n + j**n == start**n):
                print('Found')
                print('{}**{} + {}**{} = {}**{}'.format(i,n,j,n,start,n))
                found=1
                break
            else:
                print('({},{},{}) Not Satisfied'.format(i,j,start))
                continue
        if(found==1):
            break
    start = start + 1
