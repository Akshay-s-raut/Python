hex = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
        'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }

def hextodec(num):
    t = len(num)
    ans=0
    for i in num:
        ans = ans + hex[i]*(16**(t-1))
        t = t-1
    return ans

f = open("safe_to_use_unicode.txt").read()
lines = f.split('\n')

for i in lines:
    line = i.split('\t')
    print(line)

for i in lines:
    print("{}\t{}\t{}".format(i[0],i[1],i[2]))
