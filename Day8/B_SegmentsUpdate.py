
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
    while i < len(tree):
        tree[i] += d
        child = i + (i & (-i))
        i = child


def incRange(tree, x, y, d):
    inc(tree, x, d)
    inc(tree, y + 1, -d)


def getVal(tree, i):
    return getSumRange(tree, 0, i)


n, q = map(int, input().split())
a = list(map(int, input().split()))

b = [0] * (n + 1)
tree = growFWTree(b)
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        l, r, d = query[1] - 1, query[2] - 1, query[3]
        incRange(tree, l, r, d)
    else:
        i = query[1] - 1
        val = getVal(tree, i) + a[i]
        print(val)
