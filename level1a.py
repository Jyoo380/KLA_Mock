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
        for node in range(self.V):
            if (dist[node]!=0) and (node not in approached) and (dist[node]<min or min==0):
                min=dist[node]
                min_node=node
            else:
                continue
        return min_node

f=open("Y:/Student Handout/Input data/level1a.json")
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

""" for i in graph:
    print(i, end="\n") """
ord_quan=[-100]
capacity=600
paths=[]
g=Shortest_Path(g_size)
g.graph=graph
approached=[0]
for i in range(g_size):
    x=g.dijkstra(approached[i], approached)
    approached.append(x)
print(approached)
spt=[]
for i in approached:
    spt.append(neighbourhood[i])
for i in spt[1:21]:
    ord_quan.append(data["neighbourhoods"][i]["order_quantity"])
dup_app=approached
padd=[0]
c=0
for i in range(1, g_size):
    print(ord_quan)
    if(ord_quan[i]==0):
        continue
    if capacity!=0 and (approached[i]==dup_app[i] and capacity>ord_quan[i]):
        capacity-=ord_quan[i]
        ord_quan[i]=0
        padd.append(approached[i])
        dup_app[i]=0
    elif capacity!=0 and (approached[i]==dup_app[i] and ord_quan[i]>capacity):
        ord_quan[i]-=capacity
        padd.append(approached[i])
        padd.append(0)
        paths.append(padd)
        padd=[0]
        capacity=600
        i=0
        continue
    elif capacity==ord_quan[i]:
        ord_quan[i]=0
        padd.append(approached[i])
        padd.append(0)
        dup_app[i]=0
        i=0
        paths.append(padd)
        padd=[0]
        capacity==600
        continue
    if capacity==0:
        padd.append(0)
        paths.append(padd)
        continue
    for i in ord_quan:
        if i!=0:
            c+=1
    if c!=0:
        continue
    else:
        break
print(paths)
