from collections import deque
from vertex import Vertex
from graph import Graph
import math

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
        unvisited = {}
        dist = {}
        prev = {}

        dist[graph.vertices.search(0)] = 0
        unvisited[0] = graph.vertices.search(0)

        for i in range(1, len(graph.vertices)):
            dist[graph.vertices.search(i)] = (math.inf)
            prev[graph.vertices.search(i)] = None
            unvisited[i] = graph.vertices.search(i)

        i = 0
        while len(unvisited) > 0:
            neighbors = unvisited[i].neighbors
            u = min(neighbors, key=neighbors.get)
            # TODO: get the Location object that needs to be removed (after you sleep)
            unvisited.pop(u)

        #for neighbor in u.neighbors:
            # alt = Distance from WGU to u + (u + v)
            # if alt < dist[v]:
            #     dist[v] = alt
            #     prev[v] = u


        for k, v in unvisited.items():
            if k not in prev:
                if (k, v) != u:
                    temp_shortest = u[1] + abs(v - u[1])

                if temp_shortest < dist[i]:
                    dist[i] = temp_shortest
                    prev[i] = k, v
    
        unvisited.pop(prev[i][0])
        i += 1