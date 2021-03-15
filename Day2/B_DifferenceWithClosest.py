import math

na = int(input())
a = list(map(int, input().split()))
nb = int(input())
b = list(map(int, input().split()))

a.insert(0, -math.inf)
a.append(math.inf)

# print(a)


result = []
for i in range(nb):
    x = b[i]
    L = 0
    R = na + 1

    # print('----------------------------------------------------------------')
    # print('----------------------------------------------------------------')
    # print('----------------------------------------------------------------')
    #
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

    #     print('After loop (L,R):', L, ',', R)
    #
    # print('--------')
    # print('Value in A?', a[R] == x)
    if a[L] == x:
        result.append(L)
    #        print('value added', L)
    else:
        result.append(-1)
#        print('value added', -1)


# print('Result is', result)

for i in range(len(result)):
    print(result[i], end=" ")