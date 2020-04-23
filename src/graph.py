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

        # Initialize distances list with first distance from start
        dist.append(('Western Governors University 4001 South 700 East', 0.0))

        # Add all vertices (delivery stops) to unvisited list
        for vertex in self.vertices:
            uNodes.append((vertex, vertex.getDistance(dist[len(dist) - 1][0])))

        vNodes.append(uNodes.pop(0))
        nextNode = 0
        totalDist = 0

        while len(uNodes) > 0:
            # Get the nearest node
            min = math.inf
            for (vertex, distance) in uNodes:
                if distance < min:
                    min = distance
                    nextNode = uNodes.index((vertex, distance))

            currNode = uNodes.pop(nextNode)
            vNodes.append(currNode)
            dist.append((currNode[0].name, min))
            totalDist += min

            # Loop through remaining nodes in uNodes and
            # update distance
            i = 0
            for (vertex, distance) in uNodes:
                newDist = vertex.getDistance(currNode[0].name)
                uNodes[i] = (vertex, newDist)
                i += 1

        # Add return to hub
        totalDist += currNode[0].getDistance('Western Governors University 4001 South 700 East')

        for i in range(len(vNodes)):
            print(vNodes[i][0].name)
        print(totalDist)

        return totalDist