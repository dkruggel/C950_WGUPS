# David Kruggel (#001104309)

import csv
from package import Package
from location import Location
from hashtable import HashTable
from datetime import datetime
from graph import Graph
from truck import Truck

# Initialize data
package_table = HashTable(10)
location_table = HashTable(10)

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

with open('./data/WGUPS Distance Table.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',', quotechar='|')
    i = 0
    for row in file:
        s = row.split(',')
        if i != 0:
            distances = list()
            for x in range(1, 29):
                distances.append(s[x])
            location_table.insert(Location(i - 1, s[0], s[1], distances))
        i += 1

# for i in range(1, 41):
#     package = package_table.search(i)
#     print(package)

# for i in range(1, 27):
#     location = location_table.search(i)
#     print(location)

notLoaded = HashTable(10)
notLoaded = package_table.copy()

notLoaded.remove(1)

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

graph = Graph(location_table)
print(str(graph))