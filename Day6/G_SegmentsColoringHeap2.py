

def heapify(h, r, i):
    while 2 * i + 1 < len(h):
        j = 2 * i + 1
        if j + 1 < len(h) and h[j + 1][0] > h[j][0]:
            j += 1
        if h[i][0] < h[j][0]:
            h[i], h[j] = h[j], h[i]
            r[h[i][0]] = i
            r[h[j][0]] = j
            i = j
        else:
            break


def siftUp(h, r, i):
    while i > 0 and h[(i - 1) // 2][0] < h[i][0]:
        j = (i - 1) // 2
        h[i], h[j] = h[j], h[i]
        r[h[i][0]] = i
        r[h[j][0]] = j
        i = j


L, N = map(int, input().split())
e = []
color = []
for i in range(N):
    l, r, c = list(map(int, input().split()))
    if l < r:
        e.append((l, 'start', c, i))
        e.append((r, 'end', c, i))
        color.append(c)

e = sorted(e)
h = []
r = [0]*N

act = []
j = 0
ans = []
# Loop through elements
for i in range(L):
    # Loop through events
    while j < len(e) and e[j][0] == i:

        if e[j][1] == 'start':

            # Get event index and corresponding color from event list
            idx = e[j][3]
            col = e[j][2]

            # Save to end of heap
            h.append((idx, col))
            r[idx] = len(h) - 1

            # Sift value up to position
            siftUp(h, r, len(h) - 1)

        if e[j][1] == 'end':
            pos = r[e[j][3]]
            h[pos] = h[len(h) - 1]
            h.pop()

            if pos != len(h):
                r[h[pos][0]] = pos
                siftUp(h, r, pos)
                heapify(h, r, pos)

        j += 1
    if len(h) == 0:
        print(0, end=" ")
    else:
        print(h[0][1], end=" ")
