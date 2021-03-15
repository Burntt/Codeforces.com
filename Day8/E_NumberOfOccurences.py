from collections import Counter


def readInt():
    return int(input())


def readInts(k):
    n = [0] * k
    n = map(int, input().split())
    return n


def readLine():
    return list(map(int, input().split()))


# Build Tree


def growFWTree(arr):
    n = len(arr)
    tree = []
    for i in range(n + 1):
        tree.append([0, {}])
    for i in range(n):
        incBuild(tree, i, arr[i])
    return tree


def incBuild(tree, i, val):
    i += 1
    while i < len(tree):
        tree[i][0] += val
        if val not in tree[i][1]:
            tree[i][1][val] = 1
        else:
            tree[i][1][val] += 1
        child = i + (i & (-i))
        i = child


def getSum(tree, i):
    res = 0
    i += 1
    while i > 0:
        res += tree[i][0]
        parent = i - (i & (-i))
        i = parent
    return res


def getSumRange(tree, x, y):
    sumRange = getSum(tree, y) - getSum(tree, x - 1)
    return sumRange


def inc(tree, i, newv, oldv):
    d = newv - oldv
    i += 1
    while i < len(tree):
        tree[i][0] += d
        tree[i][1][oldv] -= 1
        if newv not in tree[i][1]:
            tree[i][1][newv] = 1
        else:
            tree[i][1][newv] += 1
        child = i + (i & (-i))
        i = child


def incRange(tree, x, y, d):
    inc(tree, x, d)
    inc(tree, y + 1, -d)


def getVal(tree, i):
    return getSumRange(tree, i, i)


def setVal(tree, a, idx, val_new):
    a[idx] = val_new
    val_old = getVal(tree, idx)
    inc(tree, idx, val_new, val_old)
    return tree


def buildOccMap(arr, left, right):
    segment = arr[left:right + 1]
    return Counter(segment)


def getOcc(tree, i, val):
    occ_val = 0
    i += 1
    while i > 0:
        if val in tree[i][1]:
            occ_val += tree[i][1][val]
        else:
            occ_val += 0
        parent = i - (i & (-i))
        i = parent
    return occ_val


def getOccRange(tree, x, y, val):
    occRange = getOcc(tree, y, val) - getOcc(tree, x - 1, val)
    return occRange


# Execution


n, m = readLine()
a = readLine()

treeFW = growFWTree(a)


for i in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # Replace value in fenwick tree
        pos, x = query[1], query[2]
        pos -= 1
        setVal(treeFW, a, pos, x)
    else:
        # Print query
        l, r, x = query[1], query[2], query[3]
        l -= 1
        r -= 1
        ocs = getOccRange(treeFW, l, r, x)
        print(ocs)