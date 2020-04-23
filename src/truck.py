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
        if 'Delayed' in package.notes and self.id != 3:
            return -1
        self.packages.append(package)
        package.status = 'loaded'
        return 1

    def getNextStop(self):
        return self.packages.pop()

    def __len__(self):
        return len(self.packages)