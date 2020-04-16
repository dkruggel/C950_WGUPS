from vertex import Vertex
from edge import Edge
from location import Location
from hashtable import HashTable

class Graph:
    def __init__(self, locations):
        self.edges = HashTable(50)
        k = 0
        for i in range(1, len(locations)):
            for j in range(1, len(locations)):
                vertex_start = locations.search(i)
                vertex_end = locations.search(j)
                if vertex_start != vertex_end:
                    distance = locations.search(i).getDistance(vertex_end)
                    edge = Edge(k, vertex_start, vertex_end, distance)
                    k += 1
                    self.edges.insert(edge)

    def __str__(self):
        for i in range(len(self.edges)):
            edge = self.edges.search(i)
            if self.edges.search(i) != None:
                print(edge.vertex0.name + '->' + edge.vertex1.name + ' = ' + str(edge.distance))