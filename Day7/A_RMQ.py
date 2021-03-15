import math

n = int(input())
a = list(map(int, input().split()))
m = int(input())
ops = []
for i in range(m):
    single_op = list(map(int, input().split()))
    ops.append(single_op)

treeRMQ = [math.inf] * 4 * n


def buildRMQ_Tree(a, v, l, r):
    if l == r:
        treeRMQ[v] = a[l]
    else:
        m = (l + r) // 2
        buildRMQ_Tree(a, v * 2 + 1, l, m)
        buildRMQ_Tree(a, v * 2 + 2, m + 1, r)
        treeRMQ[v] = min(treeRMQ[v * 2 + 1], treeRMQ[v * 2 + 2])


def getMin(treeRMQ, v, l, r, L, R):
    if l >= L and r <= R:
        return treeRMQ[v]
    if L > r or R < l:
        return math.inf
    m = (l + r) // 2
    min1 = getMin(treeRMQ, v * 2 + 1, l, m, L, R)
    min2 = getMin(treeRMQ, v * 2 + 2, m + 1, r, L, R)
    return min(min1, min2)


def updateRMQ(treeRMQ, v, l, r, x, t):
    if x < l or x > r:
        return
    if l ==r:
        treeRMQ[v] = t
        return
    m = (l + r) // 2
    updateRMQ(treeRMQ, v * 2 + 1, l, m, x, t)
    updateRMQ(treeRMQ, v * 2 + 2, m + 1, r, x, t)
    treeRMQ[v] = min(treeRMQ[v * 2 + 1], treeRMQ[v * 2 + 2])


buildRMQ_Tree(a, 0, 0, len(a) - 1)

getMin(treeRMQ, 0, 0, len(a) - 1, 1, 2)

for i in range(m):
    if ops[i][0] == 1:
        id = ops[i][1] - 1
        x = ops[i][2]
        updateRMQ(treeRMQ, 0, 0, len(a) - 1, id, x)
    if ops[i][0] == 2:
        qL = ops[i][1] - 1
        qR = ops[i][2] - 1
        print(getMin(treeRMQ, 0, 0, len(a) - 1, qL, qR))
