swap_ind = []


def heapify (h, n, i):
    while 3 * i + 1 < n:

        j = 3 * i + 1
        max_of_children = -10**9

        for k in range(j, j + 3):
            if k < n:
                if h[k] > max_of_children:
                    max_of_children = h[k]
                    j = k
            else:
                break

        if h[i] < h[j]:
            swap_ind.append([i, j])
            h[i], h[j] = h[j], h[i]
            i = j
        else:
            break


def heapSort(arr):
    for i in range(n - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


n = int(input())
a = list(map(int, input().split()))
heapSort(a)

print(len(swap_ind))
print(*a)