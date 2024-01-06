import json

class Shortest_Path():
    def __init__(self, vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)] for row in range(vertices)]
    
    def mindist(self, dist, spt):
        min = 1e7
        for i in range(self.V):
            if dist[i] < min and spt[i]==False:
                min = dist[i]
                min_in=i
        return min_in
    def dijkstra(self, source):
        dist=[1e7]*self.V
        dist[source]=0
        spt=[False]*self.V
        for i in range(self.V):
            u=self.mindist(dist, spt)
            spt[u]=True
            for j in range(self.V):
                if(self.graph[u][j]>0 and spt[j]==False and dist[j]>dist[u]+self.graph[u][j]):
                    dist[j]=dist[u]+self.graph[u][j]
        self.printSolution(dist)
    def printSolution(self, dist):
        print("Vertex\tDistance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

f=open("Y:/Student Handout/Input data/level0.json")
data=json.load(f)
neighbourhood=[]
for i in data["neighbourhoods"]:
    neighbourhood.append(i)
graph=[]
g_size=data["n_neighbourhoods"]+data["n_restaurants"]
g_0=[0]+data["restaurants"]["r0"]["neighbourhood_distance"]
graph.append(g_0)
for i in range(g_size):
    inn=[]
    if(i!=20):
        inn.append(data["restaurants"]["r0"]["neighbourhood_distance"][i])
    for j in range(g_size):
        inn.append(data["neighbourhoods"][neighbourhood[i-1]]["distances"][j-1])
    graph.append(inn)
g=Shortest_Path(g_size)
g.graph=graph
g.dijkstra(0)
