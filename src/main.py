# David Kruggel (#001104309)

# NEEDS
# Package class
# Data Structure

# Initialize data

# Print ALL data inside all three specified time periods

from package import Package
import csv

packages = list()

with open('./data/WGUPS Package File.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',', quotechar='|')
    for row in file:
        s = row.split(',')
        if s[0].isdigit():
            packages.append(Package(s[0], s[1], s[5], s[2], s[4], s[6], ''))

for package in packages:
    print(str(package))