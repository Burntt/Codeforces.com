from collections import defaultdict


def readInt():
    return int(input())


def readInts(k):
    n = [0] * k
    n = map(int, input().split())
    return n


def readLine():
    return list(map(int, input().split()))


def growFWTree(arr):
    n = len(arr)
    tree = [0] * (n + 1)
    for i in range(n):
        inc(tree, i, arr[i])
    return tree


def getSum(tree, i):
    res = 0
    i += 1
    while i > 0:
        res += tree[i]
        parent = i - (i & (-i))
        i = parent
    return res


def getSumRange(tree, x, y):
    sumRange = getSum(tree, y) - getSum(tree, x - 1)
    return sumRange


def inc(tree, i, d):
    i += 1
    while i < 10**18 + 10:
        tree[i] += d
        child = i + (i & (-i))
        i = child


def incRange(tree, x, y, d):
    inc(tree, x, d)
    inc(tree, y + 1, -d)


def getVal(tree, i):
    return getSumRange(tree, 0, i)


q = readInt()
tree = defaultdict(lambda: 0)
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, x = query[1], query[2]
        p -= 1
        inc(tree, p, x)
    else:
        l, r = query[1], query[2]
        l -= 1
        r -= 1
        val = getSumRange(tree, l, r)
        print(val)