import math

na = int(input())
a = list(map(int, input().split()))
nb = int(input())
b = list(map(int, input().split()))

a.insert(0, -math.inf)
a.append(math.inf)
a.sort()

#print(a)

result = []

no = 1

for i in range(nb):
    x = b[i]
    L = 0
    R = na + 1

    # print('----------------------------------------------------------------')
    # print('----------------------------------------------------------------')
    # print('----------------------------------------------------------------')
    #
    # print('a_sorted is:', a)
    # print('index number', i)
    # print('B value index:', i)
    # print('Looking for value:', x)

    while R - L > 1:
        M = L + (R - L) // 2

        # print('--------')
        # print('Before loop (L,R):', L, ',', R)
        # print('Mid is:', M)
        # print('value a[M] = ', a[M])
        # print('Changing Right bound?', a[M] > x)
        # print('Changing Left bound?', a[M] <= x)

        if a[M] > x:
            R = M
        else:
            L = M
#    print(L)
    case1 = abs(b[i] - a[L])
    case2 = abs(b[i] - a[R])
    result.append(min(case1, case2))

# print('--------')

for i in range(len(result)):
    print(result[i])
