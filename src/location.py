class Location:
    def __init__(self, id, name, address, distances):
        self.id = id
        self.name = name
        self.address = address
        self.distances = distances

    def getDistance(self, toLoc):
        return self.distances[toLoc.id + 1]

    def __str__(self):
        return str(self.id) + ': ' + self.name