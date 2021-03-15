
swap_ind = []


def heapify (h, i):
    while 2 * i + 1 < len(h):
        j = 2 * i + 1
        if j + 1 < len(h) and h[j + 1] > h[j]:
            j += 1
        if h[i] < h[j]:
            swap_ind.append([i, j])
            h[i], h[j] = h[j], h[i]
            i = j
        else:
            break
    return h, swap_ind


n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1, -1, -1):
    heapify(a, i)

print(len(swap_ind))
for k in range(len(swap_ind)):
    print(*swap_ind[k])
print(*a)