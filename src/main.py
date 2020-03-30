# David Kruggel (#001104309)

# NEEDS
# Package class
# Data Structure

# Initialize data

# Print ALL data inside all three specified time periods

from package import Package
from location import Location
import csv
from operator import itemgetter
from datetime import datetime

packages = list()
locations = list()

with open('./data/WGUPS Package File.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',', quotechar='|')
    for row in file:
        s = row.split(',')
        if s[0].isdigit():
            time = s[5]
            if time == 'EOD':
                time = datetime.strptime('23:59', '%H:%M')
            else:
                time = time[0:-3]
                time = datetime.strptime(time, '%H:%M')
            packages.append(Package(s[0], s[1], time, s[2], s[4], s[6], ''))

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

packages.sort(key=lambda Package: Package.del_deadline)

for package in packages:
    print(str(package) + str(datetime.time(package.del_deadline)))

# for location in locations:
#     print(location.name)