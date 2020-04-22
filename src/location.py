class Location:
    def __init__(self, name, address, distances):
        self.name = name
        self.address = address
        self.distances = dict(distances)

    def getDistance(self, toLoc):
        return self.distances[toLoc]