from collections import deque

class Truck:
    def __init__(self, id):
        self.id = id
        self.packages = deque()
        self.totalDistance = 0

    def addStop(self, package):
        if str(package.notes) == 'Can only be on truck 2' and self.id == 1:
            return -1
        self.packages.append(package)
        return 1
        

    def getNextStop(self):
        return self.packages.pop()

    def __len__(self):
        return len(self.packages)