from package import Package

class PackageTable:
    def __init__(self, length):
        self.array = [None] * length
        self.length = length

    # Hash function
    def hash(self, key):
        # Return the hashed key using the array length to prevent collisions
        return int(key) % self.length

    # Add to table
    def insert(self, package_id, del_address, del_deadline, del_city, del_zip, package_weight, del_status):
        # Create package object to store as value of key value pair in hash table
        package = Package(package_id, del_address, del_deadline, del_city, del_zip, package_weight, del_status)

        # Retrieve the hash index
        index = self.hash(package_id)

        # Insert package object into array
        self.array[index] = package