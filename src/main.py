# David Kruggel (#001104309)

# NEEDS
# Package class
# Data Structure

# Initialize data

# Print ALL data inside all three specified time periods

from package import Package
from location import Location
import csv

packages = list()
locations = list()

with open('./data/WGUPS Package File.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',', quotechar='|')
    for row in file:
        s = row.split(',')
        if s[0].isdigit():
            packages.append(Package(s[0], s[1], s[5], s[2], s[4], s[6], ''))

with open('./data/WGUPS Distance Table.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',', quotechar='|')
    i = 0
    for row in file:
        s = row.split(',')
        if i != 0:
            distances = list()
            for x in range(1, 29):
                distances.append(s[x])
            locations.append(Location(s[0], s[1], distances))
        i += 1

for package in packages:
    print(str(package))

for location in locations:
    print(location.name)