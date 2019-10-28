exp=input("Enter expression: ")

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

print(getCompositions(exp,'*'))
