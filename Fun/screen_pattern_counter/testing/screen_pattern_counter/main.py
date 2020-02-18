#almost works

def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

class Graph:
    g = {}
    positions = {}
    size=0
    def __init__(self,size):
        self.size=size
        count = 0
        for i in range(0,size):
            for j in range(0,size):
                self.positions[count] = (i,j)
                self.g[count] = []
                count = count + 1

        for k in range(0,size**2):
            slopes = {}
            distances = {}
            start=self.positions[k]
            for i in range(0,size**2):
                if(start!=self.positions[i] and start[0]==self.positions[i][0]):
                    if(start[1]>self.positions[i][1]):
                        if(float('-inf') in slopes):
                            slopes[float('-inf')].append(((distance(start,self.positions[i])),i))
                        else:
                            slopes[float('-inf')] = [((distance(start,self.positions[i])),i)]
                        #distances[distance(start,self.positions[i])]=i
                    else:
                        if(float('inf') in slopes):
                            slopes[float('inf')].append(((distance(start,self.positions[i])),i))
                        else:
                            slopes[float('inf')] = [((distance(start,self.positions[i])),i)]
                        #distances[((distance(start,self.positions[i])),i)]=i

                elif(start!=self.positions[i] and (self.positions[i][1]-start[1])/(self.positions[i][0]-start[0]) ==0 ):
                    if(start[0]>self.positions[i][0]):
                        if('-0' in slopes):
                            slopes['-0'].append(((distance(start,self.positions[i])),i))
                        else:
                            slopes['-0'] = [((distance(start,self.positions[i])),i)]
                    else:
                        if('+0' in slopes):
                            slopes['+0'].append(((distance(start,self.positions[i])),i))
                        else:
                            slopes['+0'] = [((distance(start,self.positions[i])),i)]

                elif(start!=self.positions[i]):
                    if((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0]) in slopes):
                        slopes[(self.positions[i][1]-start[1])/(self.positions[i][0]-start[0])].append(((distance(start,self.positions[i])),i))
                    else:
                        slopes[(self.positions[i][1]-start[1])/(self.positions[i][0]-start[0])] = [((distance(start,self.positions[i])),i)]
                    #distances[distance(start,self.positions[i])]=i
            #print(k,slopes)
            for i in slopes.items():
                mindis=float('inf')
                elem=None
                for x in i[1]:
                    if(x[0]<mindis):
                        mindis=x[0]
                        elem = x[1]
                self.g[k].append(elem)
    def DFS(self,source,length):
        visited = {}
        for i in range(0,self.size**2):
            visited[i]=False
        return self._DFS(source,length,visited.copy())

    def _DFS(self,source,length,visited):
        visited[source]=True
        if(length==0):
            return 1
        else:
            sum = 0
            for i in self.g[source]:
                if(visited[i]==False):
                    sum = sum + self._DFS(i,length-1,visited.copy())
            return sum
    def getPossiblePatterns(self):
        patterns=0
        for i in range(0,self.size**2):
            for j in range(0,9):
                patterns = patterns + self.DFS(i,j)
            print(self.DFS(i,1))
        # patterns = patterns + self.DFS(0,2)

        return patterns
f = Graph(3)
print(f.g)
# print(f.DFS(0,2))
print()
print(f.getPossiblePatterns())

'''
if(start[0]>self.positions[i][0] and start[1]>self.positions[i][0]):
    if('ul{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0])) in slopes):
        slopes['ul{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0]))].append(((distance(start,self.positions[i])),i))
    else:
        slopes['ul{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0]))] = [((distance(start,self.positions[i])),i)]
elif(start[0]>self.positions[i][0] and start[1]<self.positions[i][1]):
    if('ur{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0])) in slopes):
        slopes['ur{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0]))].append(((distance(start,self.positions[i])),i))
    else:
        slopes['ur{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0]))] = [((distance(start,self.positions[i])),i)]
elif(start[0]<self.positions[i][0] and start[1]>self.positions[i][1]):
    if('ul{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0])) in slopes):
        slopes['ll{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0]))].append(((distance(start,self.positions[i])),i))
    else:
        slopes['ll{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0]))] = [((distance(start,self.positions[i])),i)]
elif(start[0]<self.positions[i][0] and start[1]<self.positions[i][1]):
    if('ul{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0])) in slopes):
        slopes['lr{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0]))].append(((distance(start,self.positions[i])),i))
    else:
        slopes['lr{}'.format((self.positions[i][1]-start[1])/(self.positions[i][0]-start[0]))] = [((distance(start,self.positions[i])),i)]
'''
