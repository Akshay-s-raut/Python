print('knapsack : Dynamic Programming')

Weight_knapsack = int(input('Enter the size of knapsack: '))
sizes = []       # list of sizes
value = []           # list of weights
n=len(sizes)-1

def knapsack(Weight_knapsack,n):
    if n==0 or Weight_knapsack == 0:
        return 0
    if sizes[n] > Weight_knapsack:
        return knapsack(Weight_knapsack,n-1)
    else:
        return max(knapsack(Weight_knapsack,n-1),knapsack(Weight_knapsack-sizes[n],n-1) + value[n])

print(knapsack(Weight_knapsack,n))
