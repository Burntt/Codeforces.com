n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = [0] * (m + 1)

for i in range(n):
    cnt[a[i]] += 1

answer = 0
for i in range(1, m + 1):
    for j in range(1, i):
        answer += cnt[i] * cnt[j]

print(answer)