from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.V = v
        self.points = []
        self.graph = defaultdict(list)
        self.stsp = []
        self.ans = [0 for i in range(self.V + 1)]
    def addEdge(self,u,v):
        self.points.append(u)
        self.points.append(v)
        self.graph[u].append(v)
    def dfs(self):








if __name__ == "__main__":
    n,m = list(map(int,input().split()))
    g = Graph(n)
    for i  range(n):
        u,v = list(map(int,input().split()))
        g.addEdge(u,v)
    for i in range(m):
        a,b = list(map(int,input().split()))
        g.addplace(a,b)
