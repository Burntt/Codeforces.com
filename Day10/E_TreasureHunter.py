import math
from collections import deque

n, m = map(int, input().split())
field = []
s = [0, 0]
for i in range(n):
    # build field
    line = list(str(input()))
    field.append(line)
    # find start and target
    for j in range(m):
        if line[j] == '*':
            s = [i, j]

# build parent array, direction 0 - 7 to get to p[i][j] from previous state
d = []
for i in range(n):
    row = [math.inf] * m
    d.append(row)
d[s[0]][s[1]] = 0

# build  constant directions
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

queue = deque([s])
while len(queue) > 0:
    u = queue.popleft()
    for i in range(4):
        nx = u[0] + dx[i]
        ny = u[1] + dy[i]
        if 0 <= nx < n \
                and 0 <= ny < m \
                and field[nx][ny] != '1' \
                and d[nx][ny] == math.inf:
            d[nx][ny] = d[u[0]][u[1]] + 1
            queue.append((nx, ny))

# Reconstruct path
ans = -1
min_d = math.inf
k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if min_d > d[x][y]:
        min_d = d[x][y]
        ans = i + 1
print(ans)
