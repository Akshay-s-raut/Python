print('Convert any Boolean expression to Sop')
print('#Note: take conjugate of "A" as "a" ')
print()
exp=input('Enter the expression: ')

def sop(exp):

    terms =[i.lstrip().rstrip() for i in exp.split('+')]
    counts=dict()

    counts_for_n=dict()

    for i in terms:
        for j in i:
            counts[j] = counts.get(j,0) + 1

    all_variables=list()
    for i in counts:
        if(i.upper() not in all_variables):
            all_variables.append(i)
    n = len(all_variables)


    new_terms=list()
    for i in terms:
        if(len(i)<n):
            missing_variables=list()
            for j in all_variables:
                j_copy=j
                if((j_copy or j_copy.lower()) not in i):
                    missing_variables.append(j.upper())


            s=i
            new_exp=list()
            new_exp.append(s)
            for j in missing_variables:
                new_exp2 = list()
                for k in new_exp:
                    s1 = k + j.lower()
                    s2 = k + j.upper()
                    new_exp2.append(s1)
                    new_exp2.append(s2)
                new_exp = new_exp2

            for j in new_exp:
                new_terms.append(j)
        else:
            new_terms.append(i)

    new_terms_temp = list()
    for i in new_terms:
        templ=list()
        for j in i:
            templ.append(j)
        templ.sort()
        s=''
        for j in templ:
            s = s + j
        s.lstrip()
        if(s not in new_terms_temp):
            new_terms_temp.append(s)
    new_terms = new_terms_temp

    sop_exp=''
    for i in new_terms:
        templ=list()
        for j in i:
            templ.append(j)
        templ.sort()
        s=''
        for j in templ:
            s = s + j
        s.lstrip()
        sop_exp = sop_exp + ' + ' + s
    sop_exp = sop_exp[3:]
    sop_exp.lstrip()
    sop_exp.rstrip()
    return sop_exp

print(sop(exp))
