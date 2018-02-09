from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.V = v
        self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def find_par(self,parent,i):
        if parent[i] == i:
            return i
        return self.find_par(parent,parent[i])
    def union(self,parent,x,y):
        x_set = self.find_par(parent,x)
        y_set = self.find_par(parent,y)
        parent[x_set] = y_set


    def kruskal_algorithm(self):
        e = 0
        result = []
        parent = []
        weight = 0
        for i in range(self.V):
            parent.append(i)
        self.graph = sorted(self.graph,key = lambda x: x[2])
        i = 0
        while e<self.V-1:
            u,v,w = self.graph[i]
            i = i+1
            x = self.find_par(parent,u)
            y = self.find_par(parent,v)

            if(x!=y):
                e = e+1
                result.append([u,v,w])
                weight = weight + w
                self.union(parent,x,y)
        return weight


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print(g.kruskal_algorithm())
