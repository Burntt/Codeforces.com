import math


def dijkstra(g, V, src):
    d = [math.inf] * V
    d[src] = 0
    p = [-1] * V
    p[src] = src
    visited = [False] * V

    while True:
        # find u: unvisited vertex with minimal d[u]
        u = -1
        for i in range(V):
            if not visited[i] and (u == -1 or d[u] > d[i]):
                u = i

        # If no such u, break
        if u == -1 or d[u] == math.inf:
            break

        # If such u, update values of connected vertices
        visited[u] = True
        for v, w in g[u]:
            if d[v] > d[u] + w:
                p[v] = u
                d[v] = d[u] + w
    return d


n, m, v1, v2 = map(int, input().split())
v1 -= 1
v2 -= 1
g = [[] for i in range(n)]
for i in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, w])
    g[b].append([a, w])

d = dijkstra(g, n, v1)
if d[v2] == math.inf:
    print(-1)
else:
    print(d[v2])
