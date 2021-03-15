n, L, R = map(int, input().split())
a = list(map(int, input().split()))
a = a[::-1]


def f(x):
    y = 0
    for c in a:
        y = y * x + c
    return y


nsegments = 1000
answer = 10e100
for i in range(nsegments):
    l = L + (R - L) / nsegments * i
    r = l + (R - L) / nsegments
    for it in range(100):
        ml = (2 * l + r) / 3
        mr = (l + 2 * r) / 3
        if f(ml) < f(mr):
            r = mr
        else:
            l = ml
    answer = min(answer, f((l+r) / 2))

print(answer)
