functions = {'sin()':'cos()','cos()':'-sin()','tan()':'sec^2()',
'sec()':'sec()*tan()','cosec()':'-cosec()*cot()','cot()':'-cosec^2()','ln(arg)':'arg(-1)','e()':'e()','x()':'','x':'1'}


print("Indefinite Differentition")
exp=input("Enter the expression: ")

def outer_function_finder(function):
    for i in range(0,len(function)):
        if function[i]=='(':
            first = i
            break
    return [function[:i+1]+')',first]

#+ Differentition(function[outer_function_finder(function)[1]+1:-1]) not a good idea

def chain_rule(function):
    if function=='x':
        return 1
    else:
        return functions[outer_function_finder(function)[0]][:-2] + function[outer_function_finder(function)[1]:]


def uv_rule(term):
    term_derivative=list()
    functions_list = [i.lstrip().rstrip() for i in exp.split('*')]
    for i in range(0,len(functions_list)):
        if('/' not in function_list[i]):
            s = chain_rule(functions_list[i])
        
        for j in range(0,len(functions_list)):
            if i!=j:
                s = s + '*' + functions_list[j]
                term_derivative.append(s)

    return term_derivative

def uBYv_rule():
    return 0


def Differentition(exp):
    terms = [i.lstrip().rstrip() for i in exp.split('+')]
    for i in range(0,len(terms)):
        if ' ' in terms[i]:
            p = [i.lstrip().rstrip() for i in terms[i].split()]
            terms = terms[:i] + terms[i+1:]
            for i in p:
                terms.append(i)
    ans=list()
    for i in terms:
        if '/' not in i:
            ans.append(uv_rule(i))
        else:
            ans.append(uBYv_rule(i))

    print(terms)
    s = ''
    for i in ans:
        for j in i:
            s = s + ' + ' + j
    print(s.lstrip()[2:])
Differentition(exp)
