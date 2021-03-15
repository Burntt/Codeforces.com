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
        self.adj[w].append(v)

    def DFS(self, track, v, visited):

        visited[v] = True
        track.append(v)

        for i in self.adj[v]:
            if not visited[i]:
                track = self.DFS(track, i, visited)
        return track

    def connectedComponents(self, n):
        answer = [-1] * n
        visited = [False for i in range(self.V)]
        for i in range(self.V):
            if not visited[i]:
                track = []
                track = self.DFS(track, i, visited)
                for j in track:
                    answer[j] = len(track)
        return answer


############################################################################


def solve():
    # Read input data
    n, m = readLine()
    g = Graph(n)
    for i in range(m):
        v, u = readLine()
        v -= 1
        u -= 1
        g.addEdge(v, u)
    answer = g.connectedComponents(n)

    for i in range(n):
        print(answer[i], end=" ")


sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(8 * 10 ** 7)
t = threading.Thread(target=solve)
t.start()
t.join()

