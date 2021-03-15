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


class Graph():

    def __init__(self, V):
        self.V = V
        init = []
        for i in range(V):
            init.append([])
        self.graph = init

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def cyclicTest(self, v, visited, parent):

        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                if self.cyclicTest(i, visited, v):
                    return True
            elif i != parent:
                return True
            
        return False

    def isTree(self):
        visited = [False] * self.V

        if self.cyclicTest(0, visited, -1):
            return False

        for i in range(self.V):
            if not visited[i]:
                return False

        return True


############################################################################


def solve():
    # Read input data
    N = readInt()
    gM = []
    for i in range(N):
        line = readLine()
        gM.append(line)

    # Create graph
    g = Graph(N)
    for i in range(N):
        for j in range(N):
            if gM[i][j] == 1:
                g.addEdge(i, j)
    print("YES" if g.isTree() == True else "NO")


sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(8 * 10 ** 7)
t = threading.Thread(target=solve)
t.start()
t.join()
