n = int(input())
s = list(str(input()))

k = 0
i = 0
ans = []
while k < len(s):
    ans.append(s[k])
    i += 1
    k = k + i

print(''.join(ans))
