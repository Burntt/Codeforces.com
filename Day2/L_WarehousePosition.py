import math


def penalty_point(x, coord, t):
    penalty = [0] * n
    d = 0
    for i in range(n):
        d = abs(x - coord[i])
        if t[i] == 1:
            penalty[i] = d
        if t[i] == 2:
            penalty[i] = d * math.log(d + 1)
        if t[i] == 3:
            penalty[i] = d * math.sqrt(d)
        if t[i] == 4:
            penalty[i] = d ** 2
    total_penalty = sum(penalty)
    return total_penalty


def ternary_search(penalty_point, left, right, absolute_precision) -> float:
    while abs(right - left) >= absolute_precision:

        left_third = left + (right - left) / 3
        right_third = right - (right - left) / 3

        if penalty_point(left_third, coord, t) >= penalty_point(right_third, coord, t):
            left = left_third
        else:
            right = right_third
    return (left + right) / 2.0


n = int(input())
offices = []
for i in range(n):
    x, t = map(int, input().split())
    offices.append((x, t))

coord = list(map(lambda item: item[0], offices))
t = list(map(lambda item: item[1], offices))

left = min(coord) - 10
right = max(coord) + 10
absolute_precision = 10 ** (-6)

result = ternary_search(penalty_point, left, right, absolute_precision)

penalty_res = penalty_point(result, coord, t)

print(penalty_res)
print(result)