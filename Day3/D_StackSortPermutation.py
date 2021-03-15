import sys


def check_sortable(p, n):
    S = []
    maxOut = -1
    out = []
    while len(p) != 0:
        # print('============ New it =========== (', i, ')')
        # print('p = ', p)
        # print('S =', S)
        # print('out =', out)
        if len(S) != 0:
            topS = S[-1]
            # print('entering while loop?:', topS == maxOut + 1)
            # print('maxout =', maxOut)
            # print('topS = ', S)
            while topS == maxOut + 1:
                maxOut = maxOut + 1
                # print('popping from S to out')
                out.append(S.pop())

                if len(S) == 0:
                    break
                topS = S[-1]

            # print('stack after while loop:', S)
            if len(S) == 0:
                S.append(p[0])
            else:
                topS = S[-1]
                # print('p[0] = ', p[0])
                # print('topS =',   topS)
                if p[0] < topS:
                    S.append(p[0])
                    p.pop(0)
                else:
                    return 'NO'
        else:
            # print('apply step A')
            S.append(p[0])
            p.pop(0)
    return 'YES'


t = int(input())
test_cases = []
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append((n, p))

answers = []
for i in range(t):
    n = test_cases[i][0]
    p = test_cases[i][1]
    steps = sys.getsizeof(p) // sys.getsizeof(p[0])
    ansx = check_sortable(p, steps)
    print(ansx)
