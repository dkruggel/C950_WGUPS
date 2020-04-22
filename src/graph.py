from vertex import Vertex
import math

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def addVertex(self, location):
        self.vertices[location] = Vertex(location)

    def addEdge(self, vertex0, vertex1, distance):
        self.edges[(vertex0, vertex1)] = distance

    def Dijkstra(self):
        # Initial list of nodes that have not been visited
        uNodes = []

        # List of nodes that have been visited
        vNodes = []

        # List of total distances from beginning
        dist = []

        # Add all vertices (delivery stops) to unvisited list
        for vertex in self.vertices:
            uNodes.append(vertex)

        # Initialize distances list with first distance from start
        dist.append(('Western Governors University 4001 South 700 East', 0.0))

        while len(uNodes) > 0:
            nextNode = 0

            # Get the nearest node
            min = math.inf
            for vertex in uNodes:
                distance = vertex.getDistance(dist[nextNode][0])
                if distance < min:
                    min = distance
                    u = uNodes.pop(vertex)
                    vNodes.append(vertex)

            # Loop through remaining nodes in uNodes to find next shortest path from start
            for vertex in uNodes:
                alt = dist[nextNode][0] + vertex.getDistance(dist[1][1])
                if alt < dist[1][1]:
                    dist[1][1] = alt
                    nextNode = 1