from collections import deque
from vertex import Vertex
from graph import Graph
import math

# The truck class is responsible for managing the
# list of packages and, therefore, stops
class Truck:
    def __init__(self, id, packageList, package_table):
        self.id = id
        self.packages = []
        self.totalDistance = 0
        
        # We have passed in the manually loaded packages
        # using this list and this just adds them with
        # a helper function
        for i in packageList:
            self.addStop(package_table.search(i))

    # Helper function to add stops for each package while
    # matching criteria to prevent issues
    def addStop(self, package):
        # Obviously can't load on truck one if it can only be on truck two
        if str(package.notes) == 'Can only be on truck 2\n' and self.id == 1:
            return -1
        # Don't load a loaded package, please
        if str(package.status).startswith('loaded'):
            return -1
        # If the package has the wrong address, give it a new one
        if str(package.notes).find('Wrong') > -1:
            print('Package ' + str(package.id) + ' has the wrong address. New address is: 4580 S 2300 E')
            package.del_address = '4580 S 2300 E'
            package.del_city = 'Holladay'
            package.del_zip = '84117'
        
        # Add the packages to the list
        self.packages.append(package)

        # Change the package's status to loaded and on which truck
        package.status = 'loaded on truck ' + str(self.id)
        return 1

    # Returns the next stop/package
    def getNextStop(self, address):
        for package in self.packages:
            if package.del_address == address:
                return package

    # Finds a list of stops/packages from an address
    def find(self, address):
        p = []
        for package in self.packages:
            if package.del_address == address:
                p.append(package)
        
        return p

    # Returns a list of the packages on the truck
    def __len__(self):
        return len(self.packages)