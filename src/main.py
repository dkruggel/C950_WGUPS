# David Kruggel (#001104309)

from package import Package
from location import Location
from package_table import PackageTable
import csv
from operator import itemgetter
from datetime import datetime

locations = list()
package_table = PackageTable(40)

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
            if deadline == 'EOD':
                deadline = datetime.strptime('23:59', '%H:%M')
            else:
                deadline = deadline[0:-3]
                deadline = datetime.strptime(deadline, '%H:%M')
            package_table.insert(id, address, deadline, city, zip, weight, status)

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

# packages.sort(key=lambda Package: Package.del_deadline)

# for package in packages:
#     print(str(package) + str(datetime.time(package.del_deadline)))

# for location in locations:
#     print(location.name)