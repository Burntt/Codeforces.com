#
# n, L = map(int, input().split())
#
# matrix = []
# for i in range(n):
#     tmp = [0]*n
#     tmp = list(map(int, input().split()))
#     matrix.append(tmp)

n = 4
L = 3
matrix = []
matrix.append([1, 7, 8 ,2])
matrix.append([4, 8, 8, 7])
matrix.append([3, 9, 9, 7])
matrix.append([7, 7, 7, 6])

for i in range(n - L + 1):
    for j in range(n - L + 1):

        minimum = 10 ** 9 + 1
        sub = []

        for k in range(L):
            rowsub = matrix[i + k][j : j + L]
            if minimum > min(rowsub):
                minimum = min(rowsub)
            sub.append(rowsub)

        print(minimum, end=" ")
    print('')

