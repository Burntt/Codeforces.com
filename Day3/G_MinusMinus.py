def balance_eq(s, t):
    if len(t) > len(s):
        return 'NO'
    while len(t) != 0 and len(s) != 0:
        if t[0] == '+':
            if s[0] == '+':
                s.pop(0)
                t.pop(0)
            elif s[0] == '-':
                if len(s) > 1 and s[1] == '-':
                    s.pop(0)
                    s.pop(0)
                    t.pop(0)
                else:
                    balance = 'NO'
                    break
        elif t[0] == '-':
            if len(s) >= 1 and s[0] == '-':
                s.pop(0)
                t.pop(0)
            else:
                balance = 'NO'
                break
    if len(s) == 0 and len(t) == 0:
        balance = 'YES'
    else:
        balance = 'NO'
    return balance

k = int(input())
test_cases = []
for i in range(k):
    s = list(str(input()))
    t = list(str(input()))
    test_cases.append((s, t))
    balance = balance_eq(s, t)
    print(balance)