
class A:
    lst = list()
    def app(self,x):
        (self.lst).append(x)
    def __str__(self):
        s=''
        for i in self.lst:
            s = s + ' ' + '{}'.format(i)
        return s.strip()

one = A()
two = A()
one.app('l')
one.app('o')
print(one)
print(two)
