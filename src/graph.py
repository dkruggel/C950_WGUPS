from location import Location
from hashtable import HashTable
import csv

class Graph:
    def __init__(self, num_vertices):
        self.vertices = [[0 for column in range(num_vertices)] for row in range(num_vertices)]

        with open('./data/WGUPS Distance Table.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            r = 0
            i = 0
            j = 0
            neighbors = []
            for row in file:
                s = row.split(',')
                if r == 0:
                    for j in range(2,len(s)):
                        neighbors.append(s[j])
                else:
                    #distances = {}
                    for x in range(0, len(neighbors) - 1):
                        self.vertices[i][x] = float(s[x + 2])
                        #if s[0] != neighbors[x - 2]:
                            #distances[neighbors[x - 2]] = (s[x])
                    #self.vertices[i][x] = Location(i - 1, s[0], s[1], distances)
                    i += 1
                r += 1