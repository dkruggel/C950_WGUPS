# Our package object!
class Package:
    def __init__(self, package_id, del_address, del_deadline, del_city, del_zip, weight, status, notes):
        self.id = package_id
        self.del_address = del_address
        self.del_deadline = del_deadline
        self.del_city = del_city
        self.del_zip = del_zip
        self.weight = weight
        self.status = status
        self.notes = notes
    
    # Fancy little toString() overwrite to
    # display ID, status and address neatly    
    # O(1) time
    # O(1) space
    def __str__(self):
        return str(f"{self.id:02d}") + ': ' + str(self.status).ljust(30, ' ') + self.del_address