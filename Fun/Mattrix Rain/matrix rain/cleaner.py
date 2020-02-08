
hex = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
        'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }

def hextodec(num):
    t = len(num)
    ans=0
    for i in num:
        ans = ans + hex[i]*(16**(t-1))
        t = t-1
    return ans

f = open("unicode_ranges.txt").read()

lines = f.split('\n')
ranges = []

for i in lines:
    line = i.split('\t')
    if line[2]!='Undefined' and line[2]!='Unused':
        print('{}\t{}\t{}'.format(hextodec(line[0]),hextodec(line[1]),line[2]))
        ranges.append((hextodec(line[0]),hextodec(line[1])))

print(ranges)
