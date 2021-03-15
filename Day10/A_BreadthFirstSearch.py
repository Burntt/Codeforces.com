import sys
import threading
import math


def readInt():
    return int(input())


def readInts(k):
    n = [0] * k
    n = map(int, input().split())
    return n


def readLine():
    return list(map(int, input().split()))


class Graph:
    def __init__(self, V):
        self.V = V
        init = []
        for i in range(V):
            init.append([])
        self.adj = init

    def addEdge(self, u, v):
        self.adj[u].append(v)

    def BFS(self, s, target):
        parent = [None] * self.V
        d = [math.inf] * self.V
        queue = []
        queue.append(s)
        d[s] = 0

        while queue:
            cur = queue.pop(0)
            for nb in self.adj[cur]:
                if d[nb] == math.inf:
                    queue.append(nb)
                    d[nb] = d[cur] + 1
                    parent[nb] = cur
        return d, parent

    def rebuildPath(self, parents, b, a):
        path = []
        parents[a] = 'target'
        if parents[b] is None:
            return None
        while parents[b] != 'target':
            path.append(b)
            b = parents[b]
        path.append(b)
        return path[::-1]


############################################################################


def solve():
    # Read input data
    n, a, b = readLine()
    a -= 1
    b -= 1

    gM = []
    for i in range(n):
        line = readLine()
        gM.append(line)

    # Create graph
    g = Graph(n)
    for i in range(n):
        for j in range(n):
            if gM[i][j] == 1:
                g.addEdge(i, j)

    d, par = g.BFS(a, b)
    path = g.rebuildPath(par, b, a)

    if path is None:
        print('-1')
    else:
        print(len(path) - 1)
        for i in range(len(path)):
            print(path[i] + 1, end=" ")


sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(8 * 10 ** 7)
t = threading.Thread(target=solve)
t.start()
t.join()
