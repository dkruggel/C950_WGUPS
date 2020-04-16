from collections import deque
from vertex import Vertex
from graph import Graph

class Truck:
    def __init__(self, id):
        self.id = id
        self.packages = deque()
        self.totalDistance = 0

    def addStop(self, package):
        if str(package.notes) == 'Can only be on truck 2' and self.id == 1:
            return -1
        if package.status == 'loaded':
            return -1
        self.packages.append(package)
        package.status = 'loaded'
        return 1

    def getNextStop(self):
        return self.packages.pop()

    def __len__(self):
        return len(self.packages)

    def getBestPath(self, graph):
        unvisited = []
        for i in range(len(graph.vertices)):
            node = Vertex(graph.vertices[i].id)
            node.distanceFromInitial = -1
            node.neighbors = graph.vertices.copy()
            node.neighbors.remove(graph.vertices[i])
            unvisited.append(node)
        
        while unvisited.count > 0:
            

        # try every neighbor to find shortest

        # mark that node as visited and update distance

        # repeat until all nodes visited