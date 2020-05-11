from location import Location
import csv

# Here is the location table. This object stores the
# locations and their data as parsed from the csv file
class LocationTable:
    def __init__(self):
        self.locations = []

        # Access the csv file and loop through rows
        # to create location objects
        with open('../data/WGUPS Distance Table.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            r = 0
            locs = []
            for row in file:
                s = row.split(',')
                distances = {}
                if r == 0:
                    for i in range(2, len(s)):
                        locs.append(s[i])
                    r += 1
                else:
                    j = 0
                    for i in range(2, len(s)):
                        if s[i] != '\r\n' and s[i] != '\n' and s[i] != '':
                            distances[locs[j]] = float(s[i])
                            j += 1
                    address = str(s[1])[:-8]
                    self.locations.append(Location(s[0], address, distances))

    # Simply a lookup by address string
    def getLocation(self, address):
        for location in self.locations:
            if address in location.address:
                return location