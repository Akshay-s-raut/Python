print('Edit distances: Dyanamic Programming')

x = input('Enter the first string: ')
y = input('Enter the second string: ')

#Cost model
cost_of_insert = 1
cost_of_replace = 1
cost_of_deletion = 1

def edit_distances(x,y):

    if(len(x)==0):
        return len(y)*cost_of_insert

    if(len(y)==0):
        return len(x)*cost_of_deletion

    if(x[len(x)-1]==y[len(y)-1]):
        return edit_distances(x[:-1],y[:-1])

    else:
        return min(edit_distances(x[:],y[:-1]) + cost_of_insert ,edit_distances(x[:-1],y[:]) + cost_of_deletion ,edit_distances(x[:-1],y[:-1]) + cost_of_replace)

print(edit_distances(x,y))
