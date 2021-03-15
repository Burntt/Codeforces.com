import sys
import threading
from collections import Counter
from collections import defaultdict


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
        self.adj = defaultdict(lambda: [])
        self.asterisk = defaultdict(lambda: 'not marked')

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def DFS(self, track, v, visited):
        visited[v] = True
        track.append(v)

        for i in self.adj[v]:
            if not visited[i]:
                track = self.DFS(track, i, visited)
        return track

    def connectedComponents(self, n):
        answer = [[] for i in range(n)]
        visited = [False for i in range(self.V)]
        for i in range(self.V):
            if not visited[i]:
                track = []
                track = self.DFS(track, i, visited)
                if len(track) != 0:
                    for j in track:
                        answer[j] = track

        asterisks = self.asterisk.keys()
        for asterisk in sorted(asterisks, reverse=True):
            del answer[asterisk]

        comps = Counter([tuple(i) for i in answer])
        comps = sorted(comps.values())
        return comps


def inputToGraph(matrix, n, m):
    g = Graph(n * m)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '.':                             # empty cell

                if j != m - 1 and matrix[i][j + 1] == '.':      # step right
                    g.addEdge(m * i + j, m * i + j + 1)

                if matrix[i][j - 1] == '.' and j != 0:          # step left
                    g.addEdge(j + m * i, m * i + j - 1)

                if i != n - 1 and matrix[i + 1][j] == '.':      # step bottom
                    g.addEdge(j + m * i, m * i + j + m)

                if matrix[i - 1][j] == '.' and i != 0:           # step top
                    g.addEdge(j + m * i, m * i + j - m)

            elif matrix[i][j] == '*':                           # obstacle
                g.asterisk[j + m * i] = 'marked'
    return g

############################################################################


def solve():
    # Read input data
    n, m = readLine()
    matrix = []
    for i in range(n):
        line = list(str(input()))
        matrix.append(line)
    g = inputToGraph(matrix, n, m)
    comps = g.connectedComponents(n * m)
    print(len(comps))
    print(*comps)


sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(8 * 10 ** 7)
t = threading.Thread(target=solve)
t.start()
t.join()