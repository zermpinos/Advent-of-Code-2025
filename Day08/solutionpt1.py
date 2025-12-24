import math
from itertools import combinations

class UnionFind:
    def __init__(self, x):
        self.parent = list(range(x))
        self.size = [1] * x

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        self.size[xr] += self.size[yr]
        return True

with open('input') as f:
    points = [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]

n = len(points)
uf = UnionFind(n)

pairs = []
for i, j in combinations(range(n), 2):
    x1, y1, z1 = points[i]
    x2, y2, z2 = points[j]
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    pairs.append((dist, i, j))

pairs.sort()

for k in range(1000):
    _, i, j = pairs[k]
    uf.union(i, j)

circuit_sizes = {}
for i in range(n):
    root = uf.find(i)
    circuit_sizes[root] = uf.size[root]

# get unique sizes and sort descending
unique_sizes = sorted(set(circuit_sizes.values()), reverse=True)

result = unique_sizes[0] * unique_sizes[1] * unique_sizes[2]
print(result)
