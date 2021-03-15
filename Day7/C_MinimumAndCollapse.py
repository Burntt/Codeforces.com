import math

n = int(input())
a = list(map(int, input().split()))

treeRMQ = [math.inf] * 4 * n
treeRSQ = [0] * 4 * n


def buildRMQ_Tree(a, v, l, r):
    if l == r:
        treeRMQ[v] = a[l], l
    else:
        m = (l + r) // 2
        buildRMQ_Tree(a, v * 2 + 1, l, m)
        buildRMQ_Tree(a, v * 2 + 2, m + 1, r)

        min1, idx1 = treeRMQ[v * 2 + 1]
        min2, idx2 = treeRMQ[v * 2 + 2]
        if min1 < min2:
            treeRMQ[v] = min1, idx1
        else:
            treeRMQ[v] = min2, idx2


def buildRSQ_Tree(a, v, l, r):
    if l == r:
        treeRSQ[v] = a[l]
    else:
        m = (l + r) // 2

        buildRSQ_Tree(a, v * 2 + 1, l, m)
        buildRSQ_Tree(a, v * 2 + 2, m + 1, r)
        treeRSQ[v] = treeRSQ[v * 2 + 1] + treeRSQ[v * 2 + 2]


def getMin(treeRMQ, v, l, r, L, R):
    if l >= L and r <= R:
        return treeRMQ[v]
    if L > r or R < l:
        return math.inf, math.inf
    m = (l + r) // 2
    min1, idx1 = getMin(treeRMQ, v * 2 + 1, l, m, L, R)
    min2, idx2 = getMin(treeRMQ, v * 2 + 2, m + 1, r, L, R)
    if min1 < min2:
        return min1, idx1
    else:
        return min2, idx2


def getSum(treeRSQ, v, l, r, L, R):
    if l >= L and r <= R:
        return treeRSQ[v]
    if L > r or R < l:
        return 0
    m = (l + r) // 2
    sum1 = getSum(treeRSQ, v * 2 + 1, l, m, L, R)
    sum2 = getSum(treeRSQ, v * 2 + 2, m + 1, r, L, R)
    return sum1 + sum2


def updateRMQ(treeRMQ, v, l, r, x, t):
    if x < l or x > r:
        return
    if l == r:
        treeRMQ[v] = t, l
        return
    m = (l + r) // 2
    updateRMQ(treeRMQ, v * 2 + 1, l, m, x, t)
    updateRMQ(treeRMQ, v * 2 + 2, m + 1, r, x, t)
    min1, idx1 = treeRMQ[v * 2 + 1]
    min2, idx2 = treeRMQ[v * 2 + 2]
    if min1 < min2:
        treeRMQ[v] = min1, idx1
    else:
        treeRMQ[v] = min2, idx2


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


# Build RMQ tree to find minima in log_2_n time
buildRMQ_Tree(a, 0, 0, len(a) - 1)
#print(treeRMQ)

# Build RSQ with 1 on deleted indices to keep track of indices
b = [0]* len(a)
buildRSQ_Tree(b, 0, 0, len(b) - 1)

#print(treeRSQ)

for i in range(len(a)):
    # print('--------------------------')
    # Get minimum and index, and print
    tmp_min, tmp_idx = getMin(treeRMQ, 0, 0, len(a) - 1, 0, len(a) - 1)

    del_idx = getSum(treeRSQ, 0, 0, len(a) - 1, 0, tmp_idx)

    # print('number of deleted indexed before tmp_idx:', del_idx)
    # print('minimum is:', tmp_min)
    # print('corresponding idx:', tmp_idx - del_idx + 1)

    printed_idx = tmp_idx - del_idx + 1
    print(printed_idx)

    # Update
    updateRMQ(treeRMQ, 0, 0, len(a) - 1, tmp_idx, math.inf)
    updateRSQ(treeRSQ, 0, 0, len(a) - 1, tmp_idx, 1)
