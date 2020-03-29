class Location:
    def __init__(self, name, address, distances):
        self.name = name
        self.address = address
        self.distances = distances

    def getDistance(self, toLoc):
        return 5.0