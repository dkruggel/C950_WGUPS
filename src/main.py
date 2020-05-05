# David Kruggel (#001104309)

import csv
import math
from package import Package
from locationtable import LocationTable
from hashtable import HashTable
from datetime import datetime
from graph import Graph
from truck import Truck
import os

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
    dist_into_route_1 = 0
    dist_into_route_2 = 0
    dist_into_route_3 = 0
    # Step 1 minute increments until all packages
    # are delivered
    while time != snapshot_time:
        dist_into_route_1 += float(18 / 60)
        if time >= 65:
            dist_into_route_2 += float(18 / 60)
        if truck3Ready:
            dist_into_route_3 += float(18 / 60)

        if i < len(truck1Path) and truck3Ready == False:
            truck1_next = truck1Path[i]
            if truck1_next[1] <= dist_into_route_1:
                for package in truck1Route.truck.packages:
                    if package.del_address == truck1_next[0].address and str(package.status).startswith('loaded'):
                        currHour = math.floor((time + 480) / 60)
                        currMin = (time + 480) % 60
                        currTime = str(currHour) + ':' + f"{currMin:02d}"
                        package.status = 'delivered @ ' + currTime + ' by Truck 1'
                        i += 1
        elif truck3Ready == False:
            dist_to_hub = truck1Path[len(truck1Path) - 1][0].getDistance('Western Governors University 4001 South 700 East')
            if truck1Path[len(truck1Path) - 1][1] + dist_to_hub <= dist_into_route_1:
                truck3Ready = True
                i = 1

        if j < len(truck2Path) and time >= 65: # this is to hold truck 2 until 9:05 am
            truck2_next = truck2Path[j]
            if truck2_next[1] <= dist_into_route_2:
                for package in truck2Route.truck.packages:
                    if package.del_address == truck2_next[0].address and str(package.status).startswith('loaded'):
                        currHour = math.floor((time + 480) / 60)
                        currMin = (time + 480) % 60
                        currTime = str(currHour) + ':' + f"{currMin:02d}"
                        package.status = 'delivered @ ' + currTime + ' by Truck 2'
                        j += 1


        if i < len(truck3Path) and truck3Ready:
            truck3_next = truck3Path[i]
            if truck3_next[1] <= dist_into_route_3:
                for package in truck3Route.truck.packages:
                    if package.del_address == truck3_next[0].address and str(package.status).startswith('loaded'):
                        currHour = math.floor((time + 480) / 60)
                        currMin = (time + 480) % 60
                        currTime = str(currHour) + ':' + f"{currMin:02d}"
                        package.status = 'delivered @ ' + currTime + ' by Truck 3'
                        i += 1

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

t1 = [1,13,14,15,16,19,20,29,30,31,34]
t2 = [3,5,6,7,8,10,11,12,17,18,25,26,36,37,38,40]
t3 = [2,4,9,21,22,23,24,27,28,32,33,35,39]

# Create truck routes
truck1Route = Graph(Truck(1, t1, package_table), locations)
truck2Route = Graph(Truck(2, t2, package_table), locations)
truck3Route = Graph(Truck(3, t3, package_table), locations)

# Get best route
truck1Path = getBestPath(truck1Route)
truck2Path = getBestPath(truck2Route)
truck3Path = getBestPath(truck3Route)

# User interaction
print('Welcome to the WGUPS delivery tracker!\n1: Get snapshot of package status for all packages')
command = input('->')

while command.lower() != 'exit':
    if command == '1':
        time = input('What time for snapshot? (HH:mm)')
        getSnapshot(time)

    command = input('->')

#getSnapshot('9:25')
#getSnapshot('10:25')
#getSnapshot('12:10')

