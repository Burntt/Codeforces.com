import math

n, m = map(int, input().split())
a = list(map(int, input().split()))
ops = []
for i in range(m):
    single_op = list(map(int, input().split()))
    ops.append(single_op)

treeRSQ = [0] * 4 * n


def buildRSQ_Tree(a, v, l, r):
    if l == r:
        treeRSQ[v] = a[l]
    else:
        m = (l + r) // 2

        buildRSQ_Tree(a, v * 2 + 1, l, m)
        buildRSQ_Tree(a, v * 2 + 2, m + 1, r)
        treeRSQ[v] = treeRSQ[v * 2 + 1] + treeRSQ[v * 2 + 2]


def getSum(treeRSQ, v, l, r, L, R):
    if l >= L and r <= R:
        return treeRSQ[v]
    if L > r or R < l:
        return 0
    m = (l + r) // 2
    sum1 = getSum(treeRSQ, v * 2 + 1, l, m, L, R)
    sum2 = getSum(treeRSQ, v * 2 + 2, m + 1, r, L, R)
    return sum1 + sum2


def updateRSQ(treeRSQ, v, l, r, x, t):
    if x < l or x > r:
        return
    if l == r:
        treeRSQ[v] = t
        return
    m = (l + r) // 2
    updateRSQ(treeRSQ, v * 2 + 1, l, m, x, t)
    updateRSQ(treeRSQ, v * 2 + 2, m + 1, r, x, t)
    treeRSQ[v] = treeRSQ[v * 2 + 1] + treeRSQ[v * 2 + 2]


buildRSQ_Tree(a, 0, 0, len(a) - 1)

for i in range(m):
    # print sum of elements in range if t = 0
    if ops[i][0] == 0:
        qL = ops[i][1] - 1
        qR = ops[i][2] - 1
        print(getSum(treeRSQ, 0, 0, len(a) - 1, qL, qR))

    # set x-th element to y
    if ops[i][0] == 1:
        x = ops[i][1] - 1
        y = ops[i][2]
        updateRSQ(treeRSQ, 0, 0, len(a) - 1, x, y)