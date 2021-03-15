def ri():
    return int(input())


def rl():
    return list(map(int, input().split()))


def dfs(i, j):
    compSize = 1
    matrix[i][j] = "*"
    visit = [(i, j)]
    while visit:
        x, y = visit.pop()
        for hs in [-1, 0, 1]:
            for vs in [-1, 0, 1]:
                if abs(hs) + abs(vs) != 1:
                    continue
                newx, newy = x + hs, y + vs
                if 0 <= newx < n and \
                        0 <= newy < m and \
                        matrix[newx][newy] == ".":
                    matrix[newx][newy] = "*"
                    compSize += 1
                    visit.append((newx, newy))
    return compSize


n, m = rl()
matrix = [["0"] * m for i in range(n)]
for i in range(n):
    matrix[i] = [char for char in input()]
result = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == ".":
            result.append(dfs(i, j))
result.sort()

print(len(result))
print(*result)