

def f(t, n, p):
    for i in range(t):
        S = []
        out = 0

        S.append(p[i][0])
        init = 1

        while len(S) > 0 or init < n[i]:
            if len(S) > 0 and S[-1] == out:
                S.pop()
                out += 1
            elif init < n[i]:
                S.append(p[i][init])
                init += 1
            else:
                break

        if len(S) == 0:
            print('YES')
        else:
            print('NO')


t = int(input())
n = []
p = []
for i in range(t):
    n.append(int(input()))
    p.append(list(map(int, input().split())))

f(t, n, p)