n, m, k, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
g = []
for i in range(m):
    t, c = map(int, input().split())
    g.append((c, t, i))
g.sort()

answer = []


def can(d, cert):
    min_a_index = 0
    min_b_index = 0
    for i in range(d):
        if a[min_a_index] > a[i]:
            min_a_index = i
        if b[min_b_index] > b[i]:
            min_b_index = i
    ca = []
    cb = []
    min_a = a[min_a_index]
    min_b = b[min_b_index]
    for (c, t, index) in g:
        if t == 1:
            ca.append((c * min_a, index))
        else:
            cb.append((c * min_b, index))

    money = 0
    have = 0
    idx_a = 0
    idx_b = 0
    while have < k and money < s and (idx_a < len(ca) or idx_b < len(cb)):
        if idx_b >= len(cb) or (idx_a < len(ca) and ca[idx_a] < cb[idx_b]):
            if cert:
                answer.append((ca[idx_a][1], min_a_index))
            money += ca[idx_a][0]
            idx_a += 1
        else:
            if cert:
                answer.append((cb[idx_b][1], min_b_index))
            money += cb[idx_b][0]
            idx_b += 1
        have += 1
    return have >= k and money <= s


L = 0
R = n + 1

while R - L > 1:
    M = L + (R - L) // 2
    if (can(M, False)):
        R = M
    else:
        L = M
if R == n + 1:
    print(-1)
else:
    print(R)
    can(R, True)
    for (q, d) in answer:
        print(q + 1, d + 1, sep=" ")
