
infinity = float('inf')
def isCycle(graph):
    s = []
    source = 0
    s.append(source)
    visited = [False for i in range(0,graph.size)]
    visited[source] = True
    while(len(s)!=0):
        x = s.pop()
        for i in range(0,graph.size):
            if(graph.g[x][i]!=0 and visited[i]==False):
                s.append(i)
                visited[i] = True
            elif(graph.g[x][i]!=0 and visited[i]==True):
                return True
    return False

class graph:
    g = None
    size = None

    def __init__(self,size):
        self.size = size
        self.g = [[0 for i in range(0,size)] for j in range(0,size)]

    def __str__(self):
        s = "\t"
        for i in range(0,self.size):
            s = s + str(i) + "\t"
        s = s + "\n";
        for i in range(0,self.size):
            s = s + str(i) + "\t"
            for j in range(self.size):
                s = s + str(self.g[i][j]) + "\t";
            s = s + "\n";
        return s

    def insertEdge(self,u,v,value=1):
        self.g[u][v] = value

    def insertNode(self):
        for i in range(0,self.size):
            self.g[i].append(0)
        temp = [0 for i in range(0,self.size+1)]
        self.g.append(temp)
        self.size = self.size + 1

    def removeNode(self,u):
        self.g = self.g[:u] + self.g[u+1:]
        self.size = self.size - 1
        for i in range(0,self.size):
            self.g[i] = self.g[i][:u] + self.g[i][u+1:]

    def BFS(self,source):
        q = []
        path = []
        q.append(source)
        visited = [False for i in range(0,self.size)]
        visited[source] = True
        while(len(q)!=0):
            x = q[0]
            del q[0]
            path.append(x)
            for i in range(0,self.size):
                if(self.g[x][i]!=0 and visited[i]==False):
                    q.append(i)
                    visited[i] = True
        return path

    def DFS(self,source):
        s = []
        path = []
        s.append(source)
        visited = [False for i in range(0,self.size)]
        visited[source] = True
        while(len(s)!=0):
            x = s.pop()
            path.append(x)
            for i in range(0,self.size):
                if(self.g[x][i]!=0 and visited[i]==False):
                    s.append(i)
                    visited[i] = True
        return path

    def kruskal(self):
        spaningTree = graph(self.size)
        visited =  [[False for i in range(0,self.size)] for j in range(0,self.size)]
        edges_picked = []

        while(True):
            min_value = infinity
            min_index_u = -1
            min_index_v = -1
            for p in range(0,self.size):
                for q in range(0,self.size):
                    if(self.g[p][q]!=0 and self.g[p][q]<min_value and visited[p][q]==False):
                        min_value = self.g[p][q]
                        min_index_u = p
                        min_index_v = q

            if(min_value==infinity):
                break
            visited[min_index_u][min_index_v] = True
            visited[min_index_v][min_index_u] = True
            spaningTree.insertEdge(min_index_u,min_index_v,min_value)
            if(isCycle(spaningTree)):
                spaningTree.insertEdge(min_index_u,min_index_v,0)
            else:
                edges_picked.append([min_index_u,min_index_v])
        return edges_picked

    def prim(self,source=0):
        spaningTree = graph(self.size)
        included = [False for i in range(0,self.size)]
        notIncluded = [True for i in range(0,self.size)]

        included[source] = True
        notIncluded[source] = False
        edges_picked = []

        while(True):
            min_value = infinity
            min_index_u = -1
            min_index_v = -1
            for p in range(0,self.size):
                for q in range(0,self.size):
                    if(self.g[p][q]!=0 and self.g[p][q]<min_value and included[p] and notIncluded[q]):
                        min_value = self.g[p][q]
                        min_index_u = p
                        min_index_v = q
            if(min_value==infinity):
                break

            included[min_index_v] = True
            notIncluded[min_index_v] = False
            spaningTree.insertEdge(min_index_u,min_index_v,min_value)
            edges_picked.append([min_index_u,min_index_v])
        return edges_picked

    def dijkstra(self,source,destination):
        included = [False for i in range(0,self.size)]
        notIncluded = [True for i in range(0,self.size)]
        distances = [infinity for i in range(0,self.size)]
        distances[source] = 0
        path = [[source] for i in range(0,self.size)]
        # path[source].append[source]
        while(True):
            min_vert = -1
            min_value = infinity
            for i in range(0,self.size):
                if(distances[i]<min_value and notIncluded[i]):
                    min_vert = i
                    min_value = distances[i]
            if(min_vert==-1):
                break
            notIncluded[min_vert]=False

            for i in range(0,self.size):
                if(self.g[min_vert][i]!=0 and (distances[min_vert]+self.g[min_vert][i]<distances[i])):
                    distances[i] = distances[min_vert]+self.g[min_vert][i]
                    path[i] = path[min_vert] + [i]

        return [distances[destination],path[destination]]
