from collections import deque
from vertex import Vertex
from graph import Graph
import math




# for i in range(len(truck1Route.vertices) - 1):
#     keys = list(truck1Route.vertices.keys())
#     v0 = truck1Route.vertices[keys[i]]
#     v1 = truck1Route.vertices[keys[i + 1]]
#     distance = v0.location.distances[v1.location.name]
#     truck1Route.addEdge(v0, v1, distance)
#     print(v0.location.name + ' -> ' + v1.location.name + ':  ' + str(distance))



class Truck:
    def __init__(self, id):
        self.id = id
        self.packages = []
        self.totalDistance = 0

    def addStop(self, package):
        if str(package.notes) == 'Can only be on truck 2\n' and self.id == 1:
            return -1
        if package.status == 'loaded':
            return -1
        if 'Delayed' in package.notes:
            return -1
        self.packages.append(package)
        package.status = 'loaded'
        return 1

    def getNextStop(self):
        return self.packages.pop()

    def __len__(self):
        return len(self.packages)

    def getBestPath(self, graph):
        dist = [math.inf] * len(graph.vertices)
        prev = [None] * len(graph.vertices)
        path = []

        dist[0] = 0

        for vertex in range(len(graph.vertices)):
            # Find the shortest edge
            min = math.inf

            for i in range(len(graph.vertices)):
                if dist[i] < min and prev[i] == None:
                    min = dist[i]
                    u = i
            
            prev[u] = vertex
            path.append(str(u) + ':' + str(min))

            for i in range(len(graph.vertices)):
                if graph.vertices[u][i] > 0 and prev[i] == None and dist[i] > dist[u] + graph.vertices[u][i]:
                    dist[i] = dist[u] + graph.vertices[u][i]

        # for node in range(len(graph.vertices)):
        #     print(node, "->", dist[node])

        for node in range(len(path)):
            print(path[node])

    def getBestPath2(self, graph):
        # Source is 0 (WGU)
        dist = [math.inf] * len(self.packages)
        prev = [None] * len(self.packages)

        vSet = []

        for package in self.packages:
            address = package.address
            vSet.append(address, 0, 0.0)

        dist[0] = 0

        # while len(vSet) > 0:
            # Get vertex with shortest total distance so far
            # u = getMin(vSet, dist[u])