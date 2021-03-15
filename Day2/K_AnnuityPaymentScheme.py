import math

s, m, p = map(int, input().split())


def canpay(x, s, m, p):
    a = 0
    b = 0
    s_left = s
    for i in range(m):
        #print('-----')
        a = s_left * p / 100
        #print('a is:' , a)
        b = x - a
        #print('b is:', b)
        s_left = s_left - b

        #print('loan left s', s_left)
    return s_left <= 0


left = -1
right = 10**9

for i in range(100):
    mid = (left + right) / 2.0
    if canpay(mid, s, m, p):
        right = mid
    else:
        left = mid

print(right)

#canpay(90, s, m, p)