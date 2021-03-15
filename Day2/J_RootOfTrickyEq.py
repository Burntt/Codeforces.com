import math

c = float(input())


def f(x, c):
    y = 4 * x + 8 * math.log(x + 1) + x * math.log(x + 1) - c
    return y > 0


L = 0
R = 10**9

for i in range(100):
    M = (L + R) / 2.0
    if f(M, c):
        R = M
    else:
        L = M

print((L + R) / 2)
