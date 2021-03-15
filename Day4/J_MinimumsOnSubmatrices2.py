
n, L = map(int, input().split())

matrix = []
for j in range(n):
    tmp = [0]*n
    tmp = list(map(int, input().split()))
    matrix.append(tmp)


def SlidingMinimum(array, windowsize):
    n = len(array)
    L = windowsize
    M = []
    minimum = min(array[0:L - 1])
    for j in range(n - L + 1):
        if array[j - 1] == minimum:
            minimum = min(array[j: j + L - 1])
        if array[j + L - 1] < minimum:
            minimum = array[j + L - 1]
        M.append(minimum)
    return M

# print(n, L)
# print(matrix)

if L == 1:
    for i in range(n):
        print(*matrix[i])
else:
    for i in range(0, n - L + 1):
        M_curr = SlidingMinimum(matrix[i], L)

        for j in range(i + 1, i + L):
            M_test = SlidingMinimum(matrix[j], L)

            for k in range(n - L + 1):
                if M_test[k] < M_curr[k]:
                    M_curr[k] = M_test[k]
        print(*M_curr)



