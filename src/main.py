# David Kruggel (#001104309)

import csv
import math
from package import Package
from locationtable import LocationTable
from hashtable import HashTable
from datetime import datetime
from graph import Graph
from truck import Truck

def getBestPath(truckRoute):
    temp = truckRoute.Dijkstra()
    truckPath = []
    for i in range(len(temp)):
        if i == 0:
            truckPath.append((temp[i][0], temp[i][1]))
        else:
            truckPath.append((temp[i][0], temp[i][1] + truckPath[i - 1][1]))
    
    return truckPath

def getSnapshot(snap_time):
    # Get time in minutes from 00:00
    snapshot_time = (int(snap_time.split(':')[0]) * 60) + \
                     int(snap_time.split(':')[1]) - \
                     480

    # Start delivering packages
    # Time = 08:00 (480 minutes)
    time = 0
    i = 1
    j = 1
    truck3Ready = False
    dist_into_route = 0
    dist_into_route_3 = 0
    # Step 1 minute increments until all packages
    # are delivered
    while time != snapshot_time:
        dist_into_route += float(18 / 60)
        if truck3Ready:
            dist_into_route_3 += float(18 / 60)

        if i < len(truck1Path) and truck3Ready == False:
            truck1_next = truck1Path[i]
            if truck1_next[1] <= dist_into_route:
                for package in truck1.packages:
                    if package.del_address == truck1_next[0].address and str(package.status).startswith('loaded'):
                        currHour = math.floor((time + 480) / 60)
                        currMin = (time + 480) % 60
                        currTime = str(currHour) + ':' + f"{currMin:02d}"
                        package.status = 'delivered @ ' + currTime + ' by Truck 1'
                        i += 1
                        break
        elif truck3Ready == False:
            dist_to_hub = truck1Path[len(truck1Path) - 1][0].getDistance('Western Governors University 4001 South 700 East')
            if truck1Path[len(truck1Path) - 1][1] + dist_to_hub <= dist_into_route:
                truck3Ready = True
                i = 1

        if j < len(truck2Path) and time >= 65: # this is to hold truck 2 until 9:05 am
            truck2_next = truck2Path[j]
            if truck2_next[1] <= dist_into_route:
                for package in truck2.packages:
                    if package.del_address == truck2_next[0].address and str(package.status).startswith('loaded'):
                        currHour = math.floor((time + 480) / 60)
                        currMin = (time + 480) % 60
                        currTime = str(currHour) + ':' + f"{currMin:02d}"
                        package.status = 'delivered @ ' + currTime + ' by Truck 2'
                        j += 1
                        break


        if i < len(truck3Path) and truck3Ready:
            truck3_next = truck3Path[i]
            if truck3_next[1] <= dist_into_route_3:
                for package in truck3.packages:
                    if package.del_address == truck3_next[0].address and str(package.status).startswith('loaded'):
                        currHour = math.floor((time + 480) / 60)
                        currMin = (time + 480) % 60
                        currTime = str(currHour) + ':' + f"{currMin:02d}"
                        package.status = 'delivered @ ' + currTime + ' by Truck 3'
                        i += 1
                        break

        time += 1

    for i in range(1, len(package_table) + 1):
        print(package_table.search(i))    

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

truck1 = Truck(1)

t1 = [1,13,14,15,16,19,20,29,30,31,34,37,40]
for i in t1:
    truck1.addStop(package_table.search(i))
#i = 1
# while len(truck1) < 18:
#     truck1.addStop(package_table.search(i))
#     i += 1
# i = 1

truck2 = Truck(2)

t2 = [2,3,4,5,7,8,10,11,12,17,18,36,38]
for i in t2:
    truck2.addStop(package_table.search(i))

# while len(truck2) < 18:
#     truck2.addStop(package_table.search(i))
#     i += 1

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

# Get best route
truck1Path = getBestPath(truck1Route)
truck2Path = getBestPath(truck2Route)

# Load remaining packages
truck3 = Truck(3)

t3 = [6,9,21,22,23,24,25,26,27,28,32,33,35,39]
for i in t3:
    truck3.addStop(package_table.search(i))

# i = 1
# while package_table.search(i) is not None:
#     truck3.addStop(package_table.search(i))
#     i += 1

truck3Route.addVertex(locations.getLocation('4001 South 700 East'))

for i in range(len(truck3.packages)):
    address = truck3.packages[i].del_address
    truck3Route.addVertex(locations.getLocation(address))

truck3Path = getBestPath(truck3Route)

#getSnapshot('9:25')
#getSnapshot('10:25')
getSnapshot('13:12')