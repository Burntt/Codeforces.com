import sys
import threading


def dfs(cur, par, curd):
    was[cur] = True
    d[cur] = curd
    fup[cur] = curd
    edge_idx = -1
    for t in adj[cur]:
        if t[0] == par:
            edge_idx = t[1]
            continue
        if not was[t[0]]:
            dfs(t[0], cur, curd + 1)
            fup[cur] = min(fup[cur], fup[t[0]])
        else:
            fup[cur] = min(fup[cur], d[t[0]])
    if edge_idx != -1 and fup[cur] >= d[cur]:
        answer.append(edge_idx)


def solve():
    global adj
    # Read input data
    n, m = map(int, input().split())
    adj = []
    for i in range(n):
        adj.append([])
    for i in range(m):
        v, u = map(int, input().split())
        v -= 1
        u -= 1
        adj[v].append((u, i))
        adj[u].append((v, i))

    global d, fup, was, answer
    d = [0] * n
    fup = [0] * n
    was = [False] * n
    answer = []
    for i in range(n):
        if was[i]:
            continue
        dfs(i, - 1, 0)
    print(len(answer))
    for i in range(len(answer)):
        print(answer[i] + 1, end=" ")
    print()


sys.setrecursionlimit(3 * 10 ** 5)
threading.stack_size(8 * 10 ** 7)
t = threading.Thread(target=solve)
t.start()
t.join()

