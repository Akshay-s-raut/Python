A = {1:(1,'A'),3:(0,'C'),2:(2,'B')}
# B = [(1,'A'),(3,'C'),(2,'Z')]
# print(sorted(A.values()))
# print(A)
# print(sorted(B))
def f(A):
    A[1]=5
    print(A)
f(A.copy())
print(A)
