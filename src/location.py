class Location:
    def __init__(self, name, address, distances):
        self.name = name
        self.address = address
        self.distances = dict(distances)

    def getDistance(self, toLoc):
        if type(toLoc) == str:
            return self.distances[toLoc]
        elif type(toLoc) == int:
            i = 0
            for k, _ in self.distances:
                if i == toLoc:
                    return self.distances[k]
                i += 1