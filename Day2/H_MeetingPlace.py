
# s = no. seconds, n = no. friends, x_array = x coords of friends, v_array = velocity of friends
def can(s, n, x_array, v_array):
    intervals = []
    for i in range(n):
        intervals.append([x_array[i] - v_array[i] * s, x_array[i] + v_array[i] * s])

    left_bound = max(list(map(lambda item: item[0], intervals)))
    right_bound = min(list(map(lambda item: item[1], intervals)))

    return left_bound < right_bound

# n = no. friends, x_array = x coords of friends, v_array = velocity of friends
def f(n, x_array, v_array):
    L = -1
    R = 10 ** 9

    for _ in range(100):
        M = L + (R - L) / 2.0
        if can(M, n, x_array, v_array):
            R = M
        else:
            L = M

    return R

n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

result = f(n, x, v)
print(result)