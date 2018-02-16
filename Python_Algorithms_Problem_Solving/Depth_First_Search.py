from collections import defaultdict

class Depth_First_Search:
    def __init__(self):
        self.graph = defaultdict(list)
        self.points = []

    def addEdge(self,v,u):
        self.points.append(v)
        self.points.append(u)
        self.graph[v].append(u)

    def dfsuntil(self,v,visited):
        visited[v]  = True
        print(v,end=" ")
        print()
        for i in self.graph[v]:
            if visited[i] == False:
                print(i)
                print(visited)
                input()
                self.dfsuntil(i,visited)
    def DFS(self,v):
        visited = [False]*len(set(self.points))
        self.dfsuntil(v,visited)
g = Depth_First_Search()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.DFS(2)
