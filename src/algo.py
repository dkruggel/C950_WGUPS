import math

l = {1:7.2,2:3.8,3:11.0,4:2.2,5:3.5,6:10.9,7:8.6,8:7.6,9:2.8,10:6.4}

dist = []
prev = []
unvisited = {}

for k, v in l.items():
    dist.append(math.inf)
    prev.append(None)
    unvisited[k] = v

i = 0
while len(unvisited) > 0:
    min_val = min(unvisited.values())
    for k, v in unvisited.items():
        if v == min_val:
            u = k, v
    unvisited.pop(u[0])

    for k, v in unvisited.items():
        if k not in prev:
            if (k, v) != u:
                temp_shortest = u[1] + abs(v - u[1])

            if temp_shortest < dist[i]:
                dist[i] = temp_shortest
                prev[i] = k, v
    
    unvisited.pop(prev[i][0])
    i += 1

for k in dist:
    print(k)