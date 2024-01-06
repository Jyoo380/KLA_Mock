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
    def dijkstra(self, source, approached):
        dist=[1e7]*self.V
        dist[source]=0
        spt=[False]*self.V
        for i in range(self.V):
            u=self.mindist(dist, spt)
            spt[u]=True
            for j in range(self.V):
                if(self.graph[u][j]>0 and spt[j]==False and dist[j]>dist[u]+self.graph[u][j]):
                    dist[j]=dist[u]+self.graph[u][j]
        x=self.printSolution(dist, approached)
        return x
    def printSolution(self, dist, approached):
        min=0
        min_node=0
        print("node\tdist")
        for node in range(self.V):
            print(node,"\t",dist[node])
            if dist[node]!=0 and node!=0 and (node not in approached) and (dist[node]<min or min==0):
                min=dist[node]
                min_node=node
        return min_node


f=open("Y:/Student Handout/Input data/level0.json")
data=json.load(f)
neighbourhood=['r0']
for i in data["neighbourhoods"]:
    neighbourhood.append(i)
graph=[]
g_size=data["n_neighbourhoods"]+data["n_restaurants"]
g_0=data["restaurants"]["r0"]["restaurant_distance"]+data["restaurants"]["r0"]["neighbourhood_distance"]
graph.append(g_0)
for i in range(g_size-1):
    inn=[]
    inn.append(data["restaurants"]["r0"]["neighbourhood_distance"][i])
    for j in data["neighbourhoods"][neighbourhood[i+1]]["distances"]:
        inn.append(j)
    graph.append(inn)

g=Shortest_Path(g_size)
g.graph=graph
approached=[0]
for i in range(len(graph)):
    x=g.dijkstra(approached[i], approached)
    approached.append(x)
print(approached)
