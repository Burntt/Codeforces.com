import sys
import threading


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

    def DFS(self, visited, parents, v, p):

        parents[v] = p
        visited[v] = True

        for i in self.adj[v]:
            if not visited[i]:
                visited, parents = self.DFS(visited, parents, i, v)
        return visited, parents

    def rebuildPath(self, parents, v):
        path = []
        if parents[v] == -1:
            return None
        while parents[v] != v:
            path.append(v)
            v = parents[v]
        path.append(v)
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

    # Run DFS from vertex A
    parents = [-1] * (n)
    visited = [False] * g.V
    visited, parents = g.DFS(visited, parents, a, a)
    path = g.rebuildPath(parents, b)

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
