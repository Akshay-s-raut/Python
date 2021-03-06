
def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

def unitVector(p1,p2):
    magnitude = ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5
    return ((p2[0]-p1[0])/magnitude,(p2[1]-p1[1])/magnitude)

class Graph:
    g = {}
    positions = {}
    size=0
    length_vs_patterns = {}
    def __init__(self,size):
        self.size=size
        count = 0
        for i in range(0,size):
            for j in range(0,size):
                self.positions[count] = (i,j)
                self.g[count] = []
                self.length_vs_patterns[count] = 0
                count = count + 1

        for k in range(0,size**2):
            unitVectors = {}
            start = self.positions[k]
            for i in range(0,size**2):
                if(k!=i):
                    #print(self.positions[k],self.positions[i])
                    if(unitVector(self.positions[k],self.positions[i]) in unitVectors):
                        unitVectors[unitVector(self.positions[k],self.positions[i])].append(((distance(start,self.positions[i])),i))
                    else:
                        unitVectors[unitVector(self.positions[k],self.positions[i])] = [((distance(start,self.positions[i])),i)]
            for i in unitVectors.items():
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
        return self._DFS(source,length,visited,self.g.copy())

    def _DFS(self,source,length,visited,g):
        visited[source]=True
        g = self.makeCorections(visited)
        if(length==0):
            return 1
        else:
            sum = 0
            for i in g[source]:
                if(visited[i]==False):
                    sum = sum + self._DFS(i,length-1,visited.copy(),g.copy())
            return sum
    def getPossiblePatterns(self):
        patterns=0
        for i in range(0,self.size**2):
            for j in range(0,self.size**2):
                temp = self.DFS(i,j)
                #print(temp)
                self.length_vs_patterns[j] = self.length_vs_patterns[j] + temp
                patterns = patterns + temp
            # print(self.DFS(i,2))
            # patterns = patterns + self.DFS(i,2)
        return patterns
    def makeCorections(self,visited):
        g={}
        for i in range(0,self.size**2):
            g[i]=[]
        for k in range(0,self.size**2):
            unitVectors = {}
            start = self.positions[k]
            for i in range(0,self.size**2):
                if(k!=i and visited[i]==False):
                    #print(self.positions[k],self.positions[i])
                    if(unitVector(self.positions[k],self.positions[i]) in unitVectors):
                        unitVectors[unitVector(self.positions[k],self.positions[i])].append(((distance(start,self.positions[i])),i))
                    else:
                        unitVectors[unitVector(self.positions[k],self.positions[i])] = [((distance(start,self.positions[i])),i)]
            for i in unitVectors.items():
                mindis=float('inf')
                elem=None
                for x in i[1]:
                    if(x[0]<mindis):
                        mindis=x[0]
                        elem = x[1]
                g[k].append(elem)
        return g
f = Graph(3)
print(f.g)
# print(f.DFS(0,2))
print()
total_patterns = f.getPossiblePatterns()
for i in f.length_vs_patterns.items():
    print("{} dots: {}".format(i[0]+1,i[1]))
print("All Possible patterns: {}".format(total_patterns))
