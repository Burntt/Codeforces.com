from collections import deque

n, m = map(int, input().split())
field = []
s = [0, 0]
f = [0, 0]
for i in range(n):
    # build field
    line = list(str(input()))
    field.append(line)

    # find start and target
    for j in range(m):
        if line[j] == 'S':
            s = [i, j]
        elif line[j] == 'F':
            f = [i, j]

# build parent array, direction 0 - 7 to get to p[i][j] from previous state
p = []
for i in range(n):
    row = [-1] * m
    p.append(row)
p[s[0]][s[1]] = -2

# build  constant directions
dx = [-1, -1, 0, +1, +1, +1, 0, -1]
dy = [0, +1, +1, +1, 0, -1, -1, -1]
dn = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']


queue = deque([s])
while len(queue) > 0:
    u = queue.popleft()
    for i in range(8):
        nd = dn[i]
        nx = u[0] + dx[i]
        ny = u[1] + dy[i]
        if 0 <= nx < n \
                and 0 <= ny < m \
                and field[nx][ny] != '#' \
                and p[nx][ny] == -1:
            p[nx][ny] = i
            queue.append((nx, ny))

# Reconstruct path
if p[f[0]][f[1]] == -1:
    print(-1)  # didn't visit the finish
else:
    path = []
    while p[f[0]][f[1]] != -2:
        d = p[f[0]][f[1]]
        path.append(dn[d])
        f[0] -= dx[d]
        f[1] -= dy[d]
    path = path[::-1]
    print(len(path))
    for name in path:
        print(name)
