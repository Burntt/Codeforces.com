import math

n = int(input())
g = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 0:
            row[j] = math.inf
    g.append(row)


def floydWarshall(V, graph):
    d = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for i in range(n):
        d[i][i] = 0
    for t in range(V):
        for u in range(V):
            for v in range(V):
                if d[u][t] < math.inf and d[t][v] < math.inf:
                    d[u][v] = max(min(d[u][v], d[u][t] + d[t][v]), -math.inf)
    return d


dist = floydWarshall(n, g)
for i in range(n):
    for j in range(n):
        if dist[i][j] == math.inf:
            dist[i][j] = 0

for i in range(n):
    print(" ".join([str(x) for x in dist[i]]))