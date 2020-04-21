from edge import Edge
from hashtable import HashTable

class Graph:
    def __init__(self, locations):
        self.vertices = HashTable(10)
        for i in range(0, len(locations)):
            self.vertices.insert(locations.search(i))