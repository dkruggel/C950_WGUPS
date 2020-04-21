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
        dist = [math.inf] * len(graph.vertices)
        prev = [None] * len(graph.vertices)

        dist[0] = 0

        for vertex in range(len(graph.vertices)):
            # Find the shortest edge
            min = math.inf

            for i in range(len(graph.vertices)):
                if dist[i] < min and prev[i] == None:
                    min = dist[i]
                    u = i
            
            prev[u] = vertex

            for i in range(len(graph.vertices)):
                if graph.vertices[u][i] > 0 and prev[i] == None and dist[i] > dist[u] + graph.vertices[u][i]:
                    dist[i] = dist[u] + graph.vertices[u][i]

        for node in range(len(graph.vertices)):
            print(node, "->", dist[node])