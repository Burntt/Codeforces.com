n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b = sorted(b)


def count(x):
    answer = 0
    for y in a:
        l = -1
        r = m
        while r - l > 1:
            mid = l + (r - l) // 2
            if b[mid] > x - y:
                r = mid
            else:
                l = mid
        answer += r
    return answer


L = -3 * 10 ** 9
R = +3 * 10 ** 9
while R - L > 1:
    M = L + (R - L) // 2
    if count(M) < k:
        L = M
    else:
        R = M
print(R)
