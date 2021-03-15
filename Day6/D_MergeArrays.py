def index_in_list(a_list, index):
    return index < len(a_list)


def insert(h, val):
    h.append(val)
    i = len(h) - 1
    while i > 0 and h[(i - 1) // 2][0] > h[i][0]:
        h[i], h[(i - 1) // 2] = h[(i - 1) // 2], h[i]
        i = (i - 1) // 2


def get_min_ele(h):
    minimum = h.pop(0)  # minimum
    if len(h) != 0:
        h.insert(0, h.pop()) # insert maximum
        n = len(h)
        heapify(h, n, 0)
    return minimum[0], minimum[1]


def heapify(h, n, i):
    while 2 * i + 1 < n:
        j = 2 * i + 1
        if j + 1 < n and h[j + 1][0] < h[j][0]:
            j += 1
        if h[i][0] > h[j][0]:
            h[i], h[j] = h[j], h[i]
            i = j
        else:
            break


def mergeLists(A, n):
    # Initialize heap
    result = []
    ptr = [0]*n
    H = []
    sorted_list = []
    for k in range(n):
        H.append((A[k][0], k))

    for k in range(n - 1, -1, -1):
        heapify(H, n, k)

    for i in range(sum(lengths)):
        val, cf = get_min_ele(H)
        sorted_list.append(val)
        ptr[cf] += 1
        if ptr[cf] < len(A[cf]):
            val2 = A[cf][ptr[cf]]
            insert(H, (val2, cf))
        else:
            continue
    return sorted_list

########################

# Input
n = int(input())
A = []
lengths = []
for k in range(n):
    tmp = list(map(int, input().split()))
    lengths.append(tmp[0])
    A.append(tmp[1:])

sorted_list = mergeLists(A, n)

print(*sorted_list)