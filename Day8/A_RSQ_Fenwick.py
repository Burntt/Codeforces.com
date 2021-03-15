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
    sumRange = getSum(treeFW, y) - getSum(tree, x - 1)
    return sumRange


def inc(tree, i, d):
    i += 1
    while i < len(tree):
        tree[i] += d
        i = i + (i & (-i))


def incRange(tree, x, y, d):
    inc(treeFW, x, d)
    inc(treeFW, y + 1, d)


def getVal(treeFW, i):
    return getSumRange(treeFW, i, i)


n, m = map(int, input().split())
a = list(map(int, input().split()))
queries = []
for i in range(m):
    queries.append(list(map(int, input().split())))

treeFW = growFWTree(a)

for k in range(m):
    t = queries[k][0]
    if t == 0:
        x = queries[k][1] - 1
        y = queries[k][2] - 1
        s = getSumRange(treeFW, x, y)
        print(s)
    else:
        x = queries[k][1] - 1
        y = queries[k][2]
        val = getVal(treeFW, x)
        inc(treeFW, x, y - val)
