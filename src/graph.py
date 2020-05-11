from vertex import Vertex
import math

# This is the graph class that will house the
# structure and methods of the route graphs
class Graph:
    def __init__(self, truck, locations):
        # This initializes the dictionary object to hold the vertices
        self.vertices = {}

        # The truck associated with this route graph
        self.truck = truck

        # We need to add the hub as a starting point
        self.addVertex(locations.getLocation('4001 South 700 East'))
        
        # Here we'll add the vertices representing the
        # stops for each package in the truck
        for i in range(len(truck.packages)):
            address = truck.packages[i].del_address
            self.addVertex(locations.getLocation(address))

    def addVertex(self, location):
        index = len(self.vertices)
        self.vertices[index] = Vertex(location)

    # This is where we use Dijkstra's algorithm to find and return the
    # optimal path (shortest distance travelled)
    # One strength of this algorithm is the ability to always determine
    # the absolute shortest path
    # Another strength of this algorithm is the number of ways you
    # could potentially implement it with different data structures
    # to achieve better performance

    # Two other algorithms that could have been used here would be A*
    # and a greedy algorithm.  This also happens to be where I wish
    # I would have gone down a different path.  I believe A* would
    # have resulted in a much more efficient application even though
    # A* doesn't find the absolute best path and only finds the best
    # path at a given moment.  A greedy algorithm also behaves similarly
    # and the efficiency would be nice in a situation where the number
    # of packages per truck increases along with the number of cities
    # and possible trucks.
    def Dijkstra(self):
        # List of nodes that have not been visited
        uNodes = []

        # List of nodes that have been visited
        vNodes = []

        # List of total distances from beginning
        dist = []

        # Initialize distances list with first distance from start
        dist.append(('Western Governors University 4001 South 700 East', 0.0))

        # Add all vertices (delivery stops) to unvisited list
        for i in range(len(self.vertices)):
            vertex = self.vertices[i].location
            uNodes.append((vertex, vertex.getDistance(dist[len(dist) - 1][0])))

        # Add the hub to the list of visited vertices
        vNodes.append(uNodes.pop(0))
        nextNode = 0
        totalDist = 0

        # While we still have unvisited nodes, we loop!
        while len(uNodes) > 0:
            # Get the nearest node
            min = math.inf
            for (vertex, distance) in uNodes:
                if distance < min:
                    min = distance
                    nextNode = uNodes.index((vertex, distance))

            # Remove the nearest node from the unvisited nodes list
            currNode = uNodes.pop(nextNode)

            # Add it to the visited nodes list, for obvious reasons
            vNodes.append(currNode)

            # Keep track of its distance
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

        # for i in range(len(vNodes)):
        #     print(vNodes[i][0].name)
        # print(totalDist)

        return vNodes, totalDist