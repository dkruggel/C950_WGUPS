# This class is used to keep track of the individual locations
# and gives us the ability to retrieve distances between a
# location and another given location
class Location:
    def __init__(self, name, address, distances):
        self.name = name
        self.address = address
        self.distances = dict(distances)

    # This helps us easily determine the distance from
    # the location object to any other given location
    def getDistance(self, toLoc):
        # Determine if we're dealing with a string (easy)
        # or an integer/index (moderately easy)
        if type(toLoc) == str:
            return self.distances[toLoc]
        elif type(toLoc) == int:
            i = 0
            for k, _ in self.distances:
                if i == toLoc:
                    return self.distances[k]
                i += 1