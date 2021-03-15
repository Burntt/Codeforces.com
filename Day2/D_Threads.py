n, k = map(int, input().split())
a = list(map(int, input().split()))

L = 0
R = max(a) + 1


def can(x):
    sum = 0
    for i in range(n):
        sum += a[i] // x
    return sum >= k


while R - L > 1:
    M = L + (R - L) // 2
    if can(M):
        L = M
    else:
        R = M
print(L)
