import sys
import threading


class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.colorArr = [-1 for i in range(self.V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def bipartiteAllV(self):
        for i in range(self.V):
            if self.colorArr[i] == -1:
                if not self.bipartiteV(i):
                    return False
        return True

    def bipartiteV(self, src):
        queue = [src]
        while queue:
            cur = queue.pop()

            # Any self loop destroys bipartite property
            if cur in self.adj[cur]:
                return False

            # for all vertices
            for t in self.adj[cur]:

                # if edge exist u -> v and edge is not visited (has no color)
                if self.colorArr[t] == -1:

                    # If color of cur is first color, assign other color to child
                    if self.colorArr[cur] == 1:
                        self.colorArr[t] = 0
                    else:
                        self.colorArr[t] = 1
                    queue.append(t)

                # If edge from u to v is there and they already have the same color
                elif self.colorArr[t] == self.colorArr[cur]:
                    return False
        return True


def solve():
    n, m = map(int, input().split())
    g = Graph(n)
    for i in range(m):
        v, u = map(int, input().split())
        v -= 1
        u -= 1
        g.addEdge(v, u)
    result = g.bipartiteAllV()

    if result:
        print("YES")
    else:
        print("NO")


sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(8 * 10 ** 7)
t = threading.Thread(target=solve)
t.start()
t.join()

