import math
from collections import deque

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append([y, c])

d = []
for i in range(n):
    row = [math.inf] * 4
    d.append(row)
d[0][0] = 0

queue = deque([(0, 0)])
while len(queue) != 0:
    u = queue.popleft()
    for e in g[u[0]]:
        if e[1] != u[1] and d[e[0]][e[1]] == math.inf:
            d[e[0]][e[1]] = d[u[0]][u[1]] + 1
            queue.append(e)

min_d = math.inf
for c in range(4):
    min_d = min(min_d, d[n - 1][c])
if min_d == math.inf:
    print(-1)
else:
    print(min_d)
