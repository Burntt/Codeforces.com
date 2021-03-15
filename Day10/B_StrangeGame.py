import sys
import threading
from collections import defaultdict
from collections import deque


def get_neighbours(x):
    neighbours = [-1] * 3
    neighbours[0] = (x + 1) % n
    neighbours[1] = (x * x + 1) % n
    neighbours[2] = (x * x * x + 1) % n
    return neighbours


def BFS(cur, end):
    visited = defaultdict(lambda: False)
    if cur == b:
        return [cur]
    visited[cur] = True
    queue = deque([(cur, [])])
    while len(queue) > 0:
        cur, path = queue.popleft()
        visited[cur] = True
        neighbours = get_neighbours(cur)
        for v in neighbours:
            if v == end:
                return path + [cur, v]
            if not visited[v]:
                visited[v] = True
                queue.append((v, path + [cur]))
    return None


############################################################################


def solve():
    global n, a, b
    n, a, b = list(map(int, input().split()))
    path = BFS(a, b)
    if path is None:
        print("-1")
    else:
        print(len(path) - 1)
        print(*path)


sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(8 * 10 ** 7)
t = threading.Thread(target=solve)
t.start()
t.join()
