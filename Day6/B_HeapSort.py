

swap_ind = []


def heapify (h, n, i):
    while 2 * i + 1 < n:
        j = 2 * i + 1
        if j + 1 < n and h[j + 1] > h[j]:
            j += 1
        if h[i] < h[j]:
            swap_ind.append([i, j])
            h[i], h[j] = h[j], h[i]
            i = j
        else:
            break


def heapSort(arr):
    m = len(arr)
    for i in range(m - 1, -1, -1):
        heapify(arr, m, i)

    for i in range(m - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


n = int(input())
a = list(map(int, input().split()))
heapSort(a)

print(len(swap_ind))
print(*a)