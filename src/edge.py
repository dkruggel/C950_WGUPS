class Edge:
    def __init__(self, id, v0, v1, distance):
        self.id = id
        self.vertex0 = v0
        self.vertex1 = v1
        self.distance = distance

    def __str__(self):
        return self.vertex0 + ' to ' + self.vertex1 + ' = ' + (self.distance)