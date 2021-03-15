
def siftUp(h, a, r, i, n):
    while i > 0 and a[h[(i - 1) // 2]] < a[h[i]]:
        j = (i - 1) // 2
        h[i], h[j] = h[j], h[i]
        r[h[i]] = i
        r[h[j]] = j
        i = j


def heapify(h, a, r, i, n):
    while 2 * i + 1 < n:
        j = 2 * i + 1
        if j + 1 < n and a[h[j + 1]] > a[h[j]]:
            j += 1
        if a[h[i]] < a[h[j]]:
            h[i], h[j] = h[j], h[i]
            r[h[i]] = i
            r[h[j]] = j
            i = j
        else:
            break


# Read data
n = int(input())
a = list(map(int, input().split()))
m = int(input())
ops = []
for i in range(m):
    op = list(map(int, input().split()))
    ops.append(op)

# Initialize h and r
h = []
r = []
for i in range(n):
    h.append(i), r.append(i)

for i in range(n - 1, -1, -1):
    heapify(h, a, r, i, len(a))

# Execute
for i in range(m):
    t = ops[i][0]
    if t == 1:
        print(a[h[0]])
    if t == 2:
        j = ops[i][1] - 1
        x = ops[i][2]
        a[j] = x
        heapify(h, a, r, r[j], n)
        siftUp(h, a, r, r[j], n)







