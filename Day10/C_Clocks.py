import sys
import threading
import math
from collections import deque

a1, b1, a2, b2 = list(map(int, input().split()))
h1, m1 = list(map(int, input().split()))
h2, m2 = list(map(int, input().split()))


def solve():
    a = [a1, a2]
    b = [b1, b2]
    d = []
    for i in range(24):
        row = [math.inf] * 60
        d.append(row)

    d[h1][m1] = 0
    queue = deque([(h1, m1)])
    while len(queue) > 0:
        u = queue.popleft()
        for i in range(2):
            h = (u[0] + a[i]) % 24
            m = (u[1] + b[i]) % 60
            if d[h][m] == math.inf:
                d[h][m] = d[u[0]][u[1]] + 1
                queue.append((h, m))

    if d[h2][m2] == math.inf:
        print(-1)
    else:
        print(d[h2][m2])


sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(8 * 10 ** 7)
t = threading.Thread(target=solve)
t.start()
t.join()
