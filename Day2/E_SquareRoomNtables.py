t = int(input())
g = []


def can(x):
    return (x // a) * (x // b) >= n


Result = []
for i in range(t):
    n, a, b = map(int, input().split())

    L = 0
    R = n * (a + b)

    while R - L > 1:
        M = L + (R - L) // 2
        if can(M):
            R = M
        else:
            L = M
    print(R)
