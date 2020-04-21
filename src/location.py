class Location:
    def __init__(self, id, name, address, neighbors):
        self.id = id
        self.name = name
        self.address = address
        self.neighbors = neighbors

    def getDistance(self, toLoc):
        return self.neighbors[toLoc][0]

    def __str__(self):
        return str(self.id) + ': ' + self.name