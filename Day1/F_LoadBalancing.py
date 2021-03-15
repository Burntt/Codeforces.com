n = int(input())
a = list(map(int, input().split()))

import math

a = sorted(a)

sum_tasks = 0
for i in range(n):
    sum_tasks = sum_tasks + a[i]

p = int(sum_tasks / n)

# sum_tasks % n is the amount of residual tasks after filling the whole capacity in perfect sense
# n1 is the amount of servers that have 1 task less than the others,
# if the distribution is not perfect

n1 = n - sum_tasks % n

ans = 0
for i in range(n1):
    if p <= a[i]:
        break
    ans = ans + p - a[i]

for i in range(n1, n):
    if a[i] > p:
        break
    ans = ans + p + 1 - a[i]

print(ans)