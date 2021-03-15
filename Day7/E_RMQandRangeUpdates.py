import math


def buildTree(tree, a, v, l, r):
    if l == r:
        tree[v][0] = a[l]
        tree[v][1] = a[l]
    else:
        m = (l + r) // 2

        # Build left and right tree
        buildTree(tree, a, v * 2 + 1, l, m)
        buildTree(tree, a, v * 2 + 2, m + 1, r)

        # Sum of left and right children
        tree[v][0] = tree[v * 2 + 1][0] + tree[v * 2 + 2][0]

        # Minima of left and right children
        tree[v][1] = min(tree[v * 2 + 1][1], tree[v * 2 + 2][1])
    return tree


def getSumAndMin(tree, v, l, r, L, R):
    if l >= L and r <= R:
        return tree[v]
    if L > r or R < l:
        return 0, math.inf
    push(tree, seg_add, v, l, r)
    m = (l + r) // 2
    sumL, minL = getSumAndMin(tree, v * 2 + 1, l, m, L, R)
    sumR, minR = getSumAndMin(tree, v * 2 + 2, m + 1, r, L, R)
    return sumL + sumR, min(minL, minR)


def update(tree, v, l, r, x, t):
    if x < l or x > r:
        return
    if l == r:
        tree[v][0] = t
        tree[v][1] = t
        return
    push(tree, seg_add, v, l, r)
    m = (l + r) // 2
    update(tree, v * 2 + 1, l, m, x, t)
    update(tree, v * 2 + 2, m + 1, r, x, t)
    tree[v][0] = tree[v * 2 + 1][0] + tree[v * 2 + 2][0]
    tree[v][1] = min(tree[v * 2 + 1][1], tree[v * 2 + 2][1])
    return tree


def updateRange(tree, seg_add, v, l, r, L, R, d):
    if R < l or L > r:
        return
    if l >= L and r <= R:
        # set sum and minimum according to change
        tree[v][0] = (r - l + 1) * d
        tree[v][1] = d

        # update diff
        seg_add[v] = d
        return
    push(tree, seg_add, v, l, r)
    m = (l + r) // 2
    updateRange(tree, seg_add, v * 2 + 1, l, m, L, R, d)
    updateRange(tree, seg_add, v * 2 + 2, m + 1, r, L, R, d)
    tree[v][0] = tree[v * 2 + 1][0] + tree[v * 2 + 2][0]
    tree[v][1] = min(tree[v * 2 + 1][1], tree[v * 2 + 2][1])
    return tree


def push(tree, seg_add, v, l, r):
    d = seg_add[v]
    if d != 0:
        # Update sums and flag of children
        m = (l + r) // 2

        # Update sums of left and right (sum_child = sum_old + addition_to_seg)
        tree[v * 2 + 1][0] += (m - l + 1) * d
        tree[v * 2 + 2][0] += (r - (m + 1) + 1) * d

        # Update minima of left and right (children of segment have same minimum)
        tree[v * 2 + 1][1] = d
        tree[v * 2 + 2][1] = d

        # Flag the segments below
        seg_add[v * 2 + 1] = d
        seg_add[v * 2 + 2] = d

        # Reset flag of current segment
        seg_add[v] = 0

##############################################################################


# Read data
n = int(input())
a = list(map(int, input().split()))
ops = []
m = int(input())
for i in range(m):
    tmp = list(map(int, input().split()))
    ops.append(tmp)

# Initialize tree
tree = []
seg_add = []
for i in range(4 * n):
    tree.append([0, math.inf])
    seg_add.append(0)
tree = buildTree(tree, a, 0, 0, len(a) - 1)

for i in range(m):
    # Get minimum of interval
    if ops[i][0] == 1:
        qL = ops[i][1] - 1
        qR = ops[i][2] - 1
        tmp_sum, tmp_min = getSumAndMin(tree, 0, 0, len(a) - 1, qL, qR)
        print(tmp_sum, tmp_min)
    # Replace all elements in segment by ops[i][3]
    if ops[i][0] == 2:
        qL = ops[i][1] - 1
        qR = ops[i][2] - 1
        qV = ops[i][3]
        updateRange(tree, seg_add, 0, 0, len(a) - 1, qL, qR, qV)


