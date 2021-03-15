
a, b, A, B, C, M = list(map(int, input().split()))


def heapify(h, i):
    while 2 * i + 1 < len(h):
        j = 2 * i + 1
        if j + 1 < len(h) and h[j + 1] > h[j]:
            j += 1
        if h[i] < h[j]:
            h[i], h[j] = h[j], h[i]
            i = j
        else:
            break
    return h


def nextInA():
    global a, b, A, B, C, M
    result = a
    c = (a * A + b * B + C) % M
    a = b
    b = c
    return result


l, r, k = list(map(int, input().split()))

h = []
for i in range(l - 1):
    nextInA()

for i in range(k):
    h.append(nextInA())

for i in range(k - 1, -1, -1):
    heapify(h, i)

for i in range(0, r):
    x = nextInA()
    if h[0] > x:
        h[0] = x
        heapify(h, 0)

h = sorted(h)
print(*h)