f=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I'
   'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

a=int(input("Enter the Number: "))
base=int(input("Enter the Base: "))

def radix(a,base):
    s=''
    while(a!=0):
        s = s + '{}'.format(f[(a%base)])
        a=a//base
    return s[::-1]

print(radix(a,base))
