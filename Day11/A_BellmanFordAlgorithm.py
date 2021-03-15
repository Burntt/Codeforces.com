import math


def BellmanFord(g, V, s):
    d = [math.inf] * V
    d[s] = 0
    p = [-1] * V
    p[s] = s
    for _ in range(V - 1):
        for u, v, w in g:
            if d[u] != math.inf and d[v] > d[u] + w:
                p[v] = u
                d[v] = d[u] + w
    return d


# Read data
n, m = map(int, input().split())
edgeList = []
for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edgeList.append([u, v, w])

d = BellmanFord(edgeList, n, 0)

# Call function for every source (every vertex)
# Print the distance to src + 1
for i in range(1, n):
    if d[i] == math.inf:
        print('NO')
    else:
        print(d[i])




