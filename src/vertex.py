class Vertex:
    def __init__(self, id):
        self.id = id
        self.distanceFromInitial = -1
        self.neighbors = []

    def __str__(self):
        return str(self.id)