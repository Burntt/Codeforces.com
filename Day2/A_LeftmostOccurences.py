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
    R = na
    #
    # print('----------------------------------------------------------------')
    # print('----------------------------------------------------------------')
    # print('----------------------------------------------------------------')
    # print('B value index:', i)
    # print('Looking for value:', x)

    while R - L > 1:
        M = L + (R - L) // 2

        # print('--------')
        # print('Before loop (L,R):', L, ',', R)
        # print('Mid is:', M)
        # print('value a[M] = ', a[M])
        # print('Changing Right bound?', a[M] >= x)
        # print('Changing Left bound?', a[M] < x)

        if a[M] >= x:
            R = M
        else:
            L = M

        # print('After loop (L,R):', L, ',', R)
        # print('--------')

    if a[R] == x:
        result.append(R)
        # print(R)
    else:
        result.append(-1)
        # print(-1)

for i in range(len(result)):
    print(result[i], end=" ")
