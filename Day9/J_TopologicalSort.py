import sys
import threading
import collections


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
        self.adj = [[] for i in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def putVertexUtil(self, visited, topSort, v):
        if visited[v]:
            return
        visited[v] = True
        for nb in self.adj[v]:
            self.putVertexUtil(visited, topSort, nb)
        topSort.append(v)

    def putVertex(self):
        topSort = []
        visited = [False for i in range(self.V)]
        for i in range(self.V):
            self.putVertexUtil(visited, topSort, i)
        topSort = topSort[::-1]

        # Check if topSort
        where = [0] * self.V
        for i in range(self.V):
            idx = topSort[i]
            where[idx] = i

        ok = True
        for v in range(self.V):
            for nb in self.adj[v]:
                if where[v] >= where[nb]:
                    ok = False

        if not ok:
            print("NO")
        else:
            print("YES")
            for i in range(self.V):
                print(topSort[i], end=" ")


############################################################################


def solve():
    # Read input data
    n, m = readLine()
    g = Graph(n)
    for i in range(m):
        v, u = readLine()
        g.addEdge(v, u)
    g.putVertex()


sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(8 * 10 ** 7)
t = threading.Thread(target=solve)
t.start()
t.join()

