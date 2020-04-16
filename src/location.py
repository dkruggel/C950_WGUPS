class Location:
    def __init__(self, id, name, address, distances):
        self.id = id
        self.name = name
        self.address = address
        self.distances = distances

    def getDistance(self, toLoc):
        
        return 5.0

    def __str__(self):
        return str(self.id) + ': ' + self.name