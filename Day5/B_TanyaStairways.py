t = int(input())
a = list(map(int, input().split()))

ones = []
for idx, shout in enumerate(a):
    c = 0
    if shout == 1:
        ones.append(idx)
ones.append(len(a))
diffones = [ones[i+1]-ones[i] for i in range(len(ones)-1)]

print(len(ones)-1)
print(*diffones)