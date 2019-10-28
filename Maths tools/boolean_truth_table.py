f=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I'
   'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def radix(a,base):
    s=''
    while(a!=0):
        s = s + '{}'.format(f[(a%base)])
        a=a//base
    return s[::-1]

def string_arranger(s):
    a=list()
    for i in s:
        a.append(i)
    a.sort()
    s=''
    for i in a:
        s = s + i
    return s.lstrip()

def position_finder(array,key):
    for i in range(0,len(array)):
        if (array[i]==key):
            pos=i
            break
    return pos

print("Truth table for the boolean expression")
print('#Note: take conjugate of "A" as "a" ')
print('#Note: U cant whole Bar [ie: use Demorgans laws]')
print()
exp=input("Enter the expression: ")
print()


def truth_table(exp):
    terms = [i.lstrip().rstrip() for i in exp.split('+')]

    counts=dict()
    for i in terms:
        for j in i:
            counts[j] = counts.get(j,0) + 1
    all_variables=list()

    for i in counts:
        if(i.upper() not in all_variables):
            all_variables.append(i.upper())
    all_variables.sort()
    n = len(all_variables)

    terms_unrepeated=list()
    positions_unrepeated=list()
    for i in range(0,len(terms)):
        if terms[i] not in all_variables:
            terms_unrepeated.append(terms[i])
            positions_unrepeated.append(i)

    table=[[] for i in range(0,n+len(terms)+1)]

    for i in range(0,2**n):
        s = radix(i,2)
        if(len(s)<n):
            zeros = '0'*(n-len(s))
            s = zeros + s
        for i in range(0,len(s)):
            table[i].append(s[i])

    for i in range(0,len(terms)):
        term_varibles=[]
        for j in terms[i]:
            term_varibles.append(j)
        for j in range(0,2**n):
            temp=1
            for jj in range(0,len(term_varibles)):
                complement_check=term_varibles[jj]
                if(complement_check.upper()==term_varibles[jj]):
                    temp = temp*int(table[position_finder(all_variables,term_varibles[jj])][j])
                else:
                    try:
                        if(table[position_finder(all_variables,term_varibles[jj])][j]=='1'):
                            temp = temp*0
                        else:
                            temp = temp*1
                    except:
                        if(table[position_finder(all_variables,term_varibles[jj].upper())][j]=='1'):
                            temp = temp*0
                        else:
                            temp = temp*1
            table[i+n].append('{}'.format(temp))

    for i in range(0,2**n):
        temp=0
        for j in range(n,n+len(terms)):
            temp = temp + int(table[j][i])
        if(temp>0):
            table[-1].append('1')
        else:
            table[-1].append('0')

    menu=list()
    for i in all_variables:
        menu.append(i.upper())
    for i in terms_unrepeated:
        menu.append(i)
    menu.append(exp)

    for i in menu:
        print('{}\t'.format(i),end='')
    print()
    for i in range(0,2**n):
        for j in range(0,n):
            print('{}\t'.format(table[j][i]),end='')
        for j in range(n,len(table)-1):
            if (j-n) in positions_unrepeated:
                print('{}\t'.format(table[j][i]),end='')
        print('{}\t'.format(table[-1][i]),end='')
        print()
    print('Number of Inputs: {}'.format(len(all_variables)))
    print('Number of terms: {}'.format(len(terms)))
truth_table(exp)
