n = int(input())

client = []
for i in range(n):
    h, m, imp = list(map(int, input().split()))
    client.append((h, m, imp))

print(client)

