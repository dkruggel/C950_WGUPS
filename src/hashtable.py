from package import Package

class HashTable:
    # This hash table is of the chaining variety
    # which requires all buckets to be lists
    def __init__(self, initial_capacity=10):
        # Initialization involves creating empty buckets
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert function

    # Find function

    # Remove function