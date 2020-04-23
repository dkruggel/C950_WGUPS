# David Kruggel (#001104309)

import csv
from package import Package
from locationtable import LocationTable
from hashtable import HashTable
from datetime import datetime
from graph import Graph
from truck import Truck

# Initialize data
package_table = HashTable(10)

locations = LocationTable()

with open('./data/WGUPS Package File.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',', quotechar='|')
    for row in file:
        s = row.split(',')
        if s[0].isdigit():
            id = s[0]
            address = s[1]
            deadline = s[5]
            city = s[2]
            zip = s[4]
            weight = s[6]
            status = ''
            notes = s[7]
            if deadline == 'EOD':
                deadline = datetime.strptime('23:59', '%H:%M')
            else:
                deadline = deadline[0:-3]
                deadline = datetime.strptime(deadline, '%H:%M')
            package_table.insert(Package(int(id), address, deadline, city, zip, weight, status, notes))

# for i in range(1, 41):
#     package = package_table.search(i)
#     print(package)

truck1 = Truck(1)
i = 1
while len(truck1) < 16:
    truck1.addStop(package_table.search(i))
    i += 1
i = 1
truck2 = Truck(2)
while len(truck2) < 16:
    truck2.addStop(package_table.search(i))
    i += 1

# Create truck routes
truck1Route = Graph()
truck2Route = Graph()
truck3Route = Graph()

# Add vertices, starting with hub (WGU)
truck1Route.addVertex(locations.getLocation('4001 South 700 East'))
truck2Route.addVertex(locations.getLocation('4001 South 700 East'))

for i in range(len(truck1.packages)):
    address = truck1.packages[i].del_address
    truck1Route.addVertex(locations.getLocation(address))

for i in range(len(truck2.packages)):
    address = truck2.packages[i].del_address
    truck2Route.addVertex(locations.getLocation(address))

totalDistance = truck1Route.Dijkstra()
totalDistance += truck2Route.Dijkstra()

# Deliver final packages
i = 1
truck3 = Truck(3)
while package_table.search(i) is not None:
    truck3.addStop(package_table.search(i))
    i += 1

truck3Route.addVertex(locations.getLocation('4001 South 700 East'))

for i in range(len(truck3.packages)):
    address = truck3.packages[i].del_address
    truck3Route.addVertex(locations.getLocation(address))

totalDistance += truck3Route.Dijkstra()

print('Total travelled distance: ', totalDistance)