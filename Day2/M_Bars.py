
# try binary search on the answer:
# is it possible to eat bars so that there is no break more than x minutes?

import math


def longest_seq(A, target):
    cnt, max_val = 0, 0
    for e in A:
        cnt = cnt + 1 if e == target else 0
        max_val = max(cnt, max_val)
    return max_val


def min_bar_count(max_break, busy):
    n = len(busy) - 1
    ptrB = 0
    eat_idx = []
    if longest_seq(busy, 1) > max_break:
        return math.inf
    elif max_break >= len(busy):
        return 0
    else:
        while ptrB != n:
            #print('-----------------------------')
            #print(ptrB)
            #print('time to eat? busy[ptrB] =', busy[ptrB] == 0)
            if busy[ptrB] == 0:
                eat_idx.append(ptrB)
                ptrB += max_break + 1
                #print('ptrB added:', ptrB)
                if ptrB >= n:
                    #print('too far, adapting ptrB')
                    ptrB = n

                #print(ptrB)
                if busy[ptrB] == 1:
                    while busy[ptrB] == 1:
                        #print('reducing ptrB')
                        ptrB -= 1
            #print(ptrB)
        eat_idx.append(ptrB)

    #print('eat_idx', eat_idx)

    return len(eat_idx)



######################################################################

n, k = map(int, input().split())
input_str = str(input())
busy = []
for i in range(n):
    busy.append(int(input_str[i]))

# n, k = 2, 2
# busy = [0, 0]
#
# print( min_bar_count(0, busy) )

L = -1
R = 10**9
while R - L > 1:
    M = L + (R - L) // 2
    if min_bar_count(M, busy) <= k:
        R = M
    else:
        L = M
print(R)