'''can't handle log() and polynomials --- and u/v rule [//and constants]
    and it will break at sin(x) - cos(x) due to spliting at + only ''' # fix these problems

functions = {'sin()':'cos()','cos()':'-sin()','tan()':'sec^2()',
'sec()':'sec()*tan()','cosec()':'-cosec()*cot()','cot()':'-cosec^2()','ln(arg)':'arg(-1)','e()':'e()','x':'1','x()':''}

exp = input("Enter the Function: ")

def getCompositions(exp,spliter):
    s=list()
    stack = 0
    start=0
    for i in range(0,len(exp)):
        if(exp[i]=='('):
            stack = stack + 1
        elif(exp[i]==')'):
            stack = stack - 1
        elif(exp[i]==spliter and stack==0):
            s.append(exp[start:i].strip())
            start=i+1
    s.append(exp[start:].strip())
    return s

def Differentition(exp):
    composite_functions = getCompositions(exp,'+')
    s = ''
    for i in composite_functions:
        for j in uv(i):
            s = s +" + "+ j
    return s.strip()[2:]


def chain_rule(term):

    if 'x' not in term:
        return '0'
    if(term=='x'):
        return '1'

    if '/' in term:
        return uBYv(term)

    for i in range(0,len(term)):
        if(term[i]=='('):
            pos = i
            break
    inner = term[pos+1:-1]
    if("(" in inner):
        return '{}*{}'.format(functions[term[:pos+1]+')'][:-1]+inner+')',"{ " + Differentition(inner) + " }")
    else:
        return functions[term[:pos+1]+')'][:-1]+inner+')'

def uv(composite_functions):
    terms = getCompositions(composite_functions,'*')
    ans = list()
    for i in range(0,len(terms)):
        s = chain_rule(terms[i])
        for j in range(0,len(terms)):
            if(i!=j):
                s = s + '*' + terms[j]
        ans.append(s)
    return ans

def uBYv(composite_functions):
    if composite_functions[0]=='(':
        term = getCompositions(composite_functions[1:-1],'/')
    else:
        term = getCompositions(composite_functions,'/')
    return '{ ' + '( {}*{} - {}*{} )/ {}**2'.format(Differentition(term[0]),term[1],Differentition(term[1]),term[0],term[1]) + ' }'

print()
print('Diffrential = ',Differentition(exp))


# breaks at :  sin(x + tan(x)/e(x) + cos(x))*cosec(x) + x
# works fine for ((sin(x)/tan(x)*e(x))/sex(x)) !
