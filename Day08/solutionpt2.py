import math

with open("input") as f:
    lines = f.read().splitlines()

junctions = [tuple(map(int, line.split(","))) for line in lines]

# union-find data structure to track circuits
parent = list(range(len(junctions)))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(y, z):
    py, pz = find(y), find(z)
    if py != pz:
        parent[py] = pz
        return True
    return False

# compute all distances between pairs of junctions
edges = []
for i in range(len(junctions)):
    for j in range(i + 1, len(junctions)):
        x1, y1, z1 = junctions[i]
        x2, y2, z2 = junctions[j]
        dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
        edges.append((dist, i, j))

edges.sort()

last_pair = None

# keep connecting until all junctions are in one circuit
for dist, i, j in edges:
    if union(i, j):
        last_pair = (i, j)
        # check if all junctions are connected
        roots = set(find(k) for k in range(len(junctions)))
        if len(roots) == 1:
            break

# compute product of X coordinates of last merged pair
x1, _, _ = junctions[last_pair[0]]
x2, _, _ = junctions[last_pair[1]]
result = x1 * x2

print(result)
