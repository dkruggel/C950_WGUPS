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
        if 'Delayed' in package.notes and self.id != 3:
            return -1
        self.packages.append(package)
        package.status = 'loaded'
        return 1

    def getNextStop(self, address):
        for package in self.packages:
            if package.del_address == address:
                return package

    def __len__(self):
        return len(self.packages)