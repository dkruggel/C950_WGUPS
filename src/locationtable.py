from location import Location
import csv

class LocationTable:
    def __init__(self):
        self.locations = []

        with open('./data/WGUPS Distance Table.csv', newline='') as file:
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
                        if s[i] != '\r\n' and s[i] != '':
                            distances[locs[j]] = float(s[i])
                            j += 1
                    address = str(s[1])[:-8]
                    self.locations.append(Location(s[0], address, distances))

    def getLocation(self, address):
        for location in self.locations:
            if address in location.address:
                return location