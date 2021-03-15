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
        i = i - (i & (-i))
    return res


def getSumRange(tree, x, y):
    sumRange = getSum(tree, y) - getSum(tree, x - 1)
    return sumRange


def inc(tree, i, d):
    i += 1
    while i < len(tree):
        tree[i] += d
        i = i + (i & (-i))


def incRange(tree, x, y, d):
    inc(tree, x, d)
    inc(tree, y + 1, -d)


def getVal(tree, i):
    return getSumRange(tree, i, i)


def argSort(seq):
    return [i for (v, i) in sorted((v, i) for (i, v) in enumerate(seq))]


n = readInt()
a = readLine()

a = argSort(a)
tree = [0] * (n + 1)

inversion = 0
for i in range(n - 1, -1, -1):
    inversion += getSum(tree, a[i] - 1)
    inc(tree, a[i], 1)

print(inversion)