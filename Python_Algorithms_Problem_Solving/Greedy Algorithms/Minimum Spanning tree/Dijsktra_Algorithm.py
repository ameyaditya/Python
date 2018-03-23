import sys

class Graph:
    def __init__(self,V):
        self.V = V
        self.graph = [[0]*V]*V
    def find_min(self,keys,setmst):
        min = float("inf")
        for loop in range(self.V):
            if keys[loop] < min and setmst[loop] == False:
                min = keys[loop]
                min_index = loop
        return min_index
    def Dijsktras_algorithm(self,src):
         keys = [float("inf")]*self.V
         keys[src] = 0
         setmst = [False]*self.V

         for count in range(self.V):
             u = self.find_min(keys,setmst)
             setmst[u] = True

             for v in range(self.V):
                 if self.graph[u][v] > 0 and setmst[v] == False and keys[v] > keys[u]+self.graph[u][v]:
                     keys[v] = keys[u]+self.graph[u][v]
         for iter in range(self.V):
             print(iter," ",keys[iter])

g  = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ]
g.Dijsktras_algorithm(3)
