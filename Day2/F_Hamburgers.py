def count_ingredients(str_in):
    B = 0
    S = 0
    C = 0
    for i in range(len(str_in)):
        if (str_in[i]) == 'B':
            B += 1
        elif str_in[i] == 'C':
            C += 1
        else:
            S += 1
    return [B, S, C]


def can(M, bcs_count, n_kitchen, p_shop, r):

    num_b = M * bcs_count[0] - n_kitchen[0]
    num_s = M * bcs_count[1] - n_kitchen[1]
    num_c = M * bcs_count[2] - n_kitchen[2]

    money = 0
    if num_b > 0:
        money += num_b * p_shop[0]
    if num_s > 0:
        money += num_s * p_shop[1]
    if num_c > 0:
        money += num_c * p_shop[2]

    return r >= money


str_in = str(input())
n_kitchen = list(map(int, input().split()))
p_shop = list(map(int, input().split()))
r = int(input())

bcs_count = count_ingredients(str_in)

L = -1
R = 10**13
ans = 0
while R - L > 1:
    M = L + (R - L) // 2
    if can(M, bcs_count, n_kitchen, p_shop, r):
        L = M
    else:
        R = M
print(L)
