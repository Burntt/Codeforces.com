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

    def __init__(self, matrix, n, m):
        self.n = n
        self.m = m
        self.matrix = matrix

    def DFS(self, comp, visited, i, j):
        n = self.n
        m = self.m
        matrix = self.matrix
        visited[i][j] = True
        comp.append((i, j))

        curr_adj = []
        if j != m - 1 and matrix[i][j + 1] == '.':  # step right
            curr_adj.append((i, j + 1))

        if matrix[i][j - 1] == '.' and j != 0:      # step left
            curr_adj.append((i, j - 1))

        if i != n - 1 and matrix[i + 1][j] == '.':  # step bottom
            curr_adj.append((i + 1, j))

        if matrix[i - 1][j] == '.' and i != 0:      # step top
            curr_adj.append((i - 1, j))

        for nb in curr_adj:
            i, j = nb[0], nb[1]
            if not visited[i][j]:
                comp = self.DFS(comp, visited, i, j)
        return comp

    def connectedComponents(self):
        answer = []
        visited = []
        for i in range(self.n):
            visited.append([False] * self.m)
            answer.append([ [] for i in range(self.m) ])

        comps = []
        for i in range(self.n):
            for j in range(self.m):
                if not visited[i][j] and self.matrix[i][j] == '.':
                    comp = []
                    comp = self.DFS(comp, visited, i, j)
                    if comp:
                        comps.append(len(comp))
        return comps


def solve():
    # Read input data
    n, m = readLine()
    matrix = []
    for i in range(n):
        line = list(str(input()))
        matrix.append(line)

    g = Graph(matrix, n, m)
    comps = g.connectedComponents()
    print(len(comps))
    print(*sorted(comps))


sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(8 * 10 ** 7)
t = threading.Thread(target=solve)
t.start()
t.join()

##