"""
A minimum spanning tree algorithm
used to generate a tree starting for initial root
helpul for dijsktra algorithm   
"""
import sys

class Graph:
    def __init__(self,Ver):
        self.V = Ver
        self.graph =[[0 for i in range(Ver)]
                    for j in range(Ver)]

    def find_min(self,keys,setmst):
        min = float("inf")

        for loop in range(self.V):
            if keys[loop] < min and setmst[loop] == False:
                min = keys[loop]
                min_index = loop
        return min_index

    def Prims_alg(self):
        keys = [float("inf")]*self.V
        keys[0] = 0
        parent = [None]*self.V
        parent[0] = -1
        setmst = [False]*self.V

        for count in range(self.V):
            u = self.find_min(keys,setmst)
            setmst[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and setmst[v] == False and keys[v] > self.graph[u][v]:
                    keys[v] = self.graph[u][v]
                    parent[v] = u
        sum = 0
        for x in range(1,self.V):
            sum = sum + self.graph[parent[x]][x]
        print (sum)

g  = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0],
           ]
g.Prims_alg()
