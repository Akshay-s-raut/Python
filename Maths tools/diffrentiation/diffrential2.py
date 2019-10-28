functions = {'sin()':'cos()','cos()':'-sin()','tan()':'sec^2()',
'sec()':'sec()*tan()','cosec()':'-cosec()*cot()','cot()':'-cosec^2()','ln(arg)':'arg(-1)','e()':'e()','x':'1','x()':''}

exp = input("Enter the Function: ")
composite_functions = [(x.lstrip()).rstrip() for x in exp.split('+')]
print(composite_functions)

def chain_rule(term):
    for i in range(0,len(term)):
        if(term[i]=='('):
            pos = i
            break
    inner = term[pos+1:-1]
    if("(" in inner):
        return '{}*{}'.format(functions[term[:pos+1]+')'][:-1]+inner+')',chain_rule(inner))
    else:
        return functions[term[:pos+1]+')'][:-1]+inner+')'

print(chain_rule(exp))
