import math
math.inf

def ri():
    return int(input())


def rl():
    return list(map(int, input().split()))


def floyd_warshall():
    d = [[math.inf] * n for i in range(n)]
    for i in range(n):
        d[i][i] = 0

    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], weights[i][j])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


n = ri()
weights = [[0] * n for i in range(n)]
for i in range(n):
    weights[i] = rl()
    for j in range(n):
        if weights[i][j] == 0:
            weights[i][j] = math.inf

d = floyd_warshall()

for i in range(n):
    for j in range(n):
        if d[i][j] == math.inf:
            d[i][j] = 0

for i in range(n):
    print(" ".join([str(x) for x in d[i]]))