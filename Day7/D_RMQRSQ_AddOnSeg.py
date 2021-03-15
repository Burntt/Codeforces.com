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


def updateRange(tree, seg_add, v, l, r, L, R, diff):
    if R < l or L > r:
        return
    if l >= L and r <= R:
        # set sum and minimum according to change
        tree[v][0] += (r - l + 1) * diff
        tree[v][1] += diff

        # update diff
        seg_add[v] += diff
        return
    push(tree, seg_add, v, l, r)
    m = (l + r) // 2
    updateRange(tree, seg_add, v * 2 + 1, l, m, L, R, diff)
    updateRange(tree, seg_add, v * 2 + 2, m + 1, r, L, R, diff)
    tree[v][0] = tree[v * 2 + 1][0] + tree[v * 2 + 2][0]
    tree[v][1] = min(tree[v * 2 + 1][1], tree[v * 2 + 2][1])
    return tree


def push(tree, seg_add, v, l, r):
    diff = seg_add[v]
    if diff != 0:
        # Update sums and flag of children
        m = (l + r) // 2

        # Update sums of left and right (sum_child = sum_old + addition_to_seg)
        tree[v * 2 + 1][0] += (m - l + 1) * diff
        tree[v * 2 + 2][0] += (r - (m + 1) + 1) * diff

        # Update minima of left and right (children of segment have same minimum)
        tree[v * 2 + 1][1] += diff
        tree[v * 2 + 2][1] += diff

        # Flag the segments below
        seg_add[v * 2 + 1] += diff
        seg_add[v * 2 + 2] += diff

        # Reset flag of current segment
        seg_add[v] = 0


####################

n, m = map(int, input().split())
a = list(map(int, input().split()))
ops = []
for i in range(m):
    tmp = list(str(input()).split())
    for k in range(1, len(tmp)):
        tmp[k] = int(tmp[k])
    ops.append(tmp)

#####################

tree = []
seg_add = []
for i in range(4 * n):
    tree.append([0, math.inf])
    seg_add.append(0)

tree = buildTree(tree, a, 0, 0, len(a) - 1)

######## EXECUTE ##########

ans = []
for i in range(m):
    if ops[i][0] == '+':
        L = ops[i][1]
        R = ops[i][2]
        d = ops[i][3]
        updateRange(tree, seg_add, 0, 0, len(a) - 1, L, R, d)
    if ops[i][0] == 'm':
        L = ops[i][1]
        R = ops[i][2]
        _, tmp_min = getSumAndMin(tree, 0, 0, len(a) - 1, L, R)
        print(tmp_min), ans.append(tmp_min)
        continue
    if ops[i][0] == 's':
        L = ops[i][1]
        R = ops[i][2]
        tmp_sum, _ = getSumAndMin(tree, 0, 0, len(a) - 1, L, R)
        print(tmp_sum), ans.append(tmp_sum)