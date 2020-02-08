import random
f=open("countries.txt").read()
countries = f.split('\n')

played = []

def greedy_player(letter):
    match = []
    for i in countries:
        if(letter.upper() == i[0].upper()) and (i not in played):
            match.append(i)
    if len(match)==0:
        return None
    c = dict()
    for i in match:
        count = 0
        for j in countries:
            if(i[-1].upper()==j[0].upper()) and (j not in played):
                count = count + 1
        c[i] = count
    x =  min(c.items(), key = lambda x: x[1])[0]
    played.append(x)
    return x

def random_player(letter):
    match = []
    for i in countries:
        if (letter.upper() == i[0].upper() ) and  (i not in played):
            match.append(i)
    if len(match)==0:
        return None
    x = random.choice(match)
    played.append(x)
    return x



def game1(choice='r'):
    start = 's'
    if(choice=='r'):
        c = 1
    elif(choice=='g'):
        c = 0
    if(c==0):
        while(True):
            x = greedy_player(start)
            if(x==None):
                return 'Random Won'
            y = random_player(x[-1])
            if(y==None):
                return 'Greedy Won'
            start = y[-1]
    else:
        while(True):
            x = random_player(start)
            if(x==None):
                return 'Greedy Won'
            y = greedy_player(x[-1])
            if(y==None):
                return 'Random Won'
            start = y[-1]
