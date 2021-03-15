n, m = map(int, input().split())

AB = []
for i in range(n):
    a, b = map(int, input().split())
    AB.append((a,b))

def can(n_songs, n, m , AB):
    sum_space = 0
    memdec = []

    if n_songs > n:
        return True

    for i in range(n):
        sum_space += AB[i][0]
        profit = AB[i][0] - AB[i][1]
        memdec.append(profit)

    memdec_sorted = sorted(memdec)

    total_dec = []
    for i in range(n_songs):
        total_dec.append(memdec_sorted.pop())

    return sum_space - sum(total_dec) <= m


def binary_search(n, m, AB):
    L = -1
    R = n + 1
    sum_comp = 0
    for i in range(n):
        sum_comp += AB[i][1]

    if sum_comp > m:
        return -1
    else:
        while R - L > 1:
            M = L + (R - L) // 2
            if can(M, n, m , AB):
                R = M
            else:
                L = M
    return R

print( binary_search(n, m, AB) )
