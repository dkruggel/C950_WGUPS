# David Kruggel #001104309

# NEEDS
# Package class
# Data Structure

# Initialize data

# Print ALL data inside all three specified time periods

class Package:
    def __init__(self, package_id, del_address, del_deadline, del_city, del_zip, weight, status):
        self.id = package_id
        self.del_address = del_address
        self.del_deadline = del_deadline
        self.del_city = del_city
        self.del_zip = del_zip
        self.weight = weight
        self.status = status
    
    def __str__(self):
        return str(self.id) + ': ' + self.status

package = Package(1, '123 Main Street', '03/28/20', 'Anywhere', '55555', 22.4, 'Out for delivery')

print(str(package))