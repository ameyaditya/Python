from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def find_par(self,parent,i):
        if parent[i] == -1:
            return i
        else:
            return self.find_par(parent,parent[i])

    def union(self,parent,x,y):
        x_set = self.find_par(parent,x)
        y_set = self.find_par(parent,y)
        parent[x_set] = y_set

    def find_cycle(self):
        parent = [-1]*self.v
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_par(parent,i)
                y = self.find_par(parent,j)
                if x == y:
                    return True
                self.union(parent,x,y)
g = Graph(3)
g.addedge(0,1)
g.addedge(1,2)
g.addedge(2,0)

if(g.find_cycle() == True):
    print("cycle found.")
else:
    print("no cycle.")
