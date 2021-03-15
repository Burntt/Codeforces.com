L, N = map(int, input().split())
e = []
for i in range(N):
    l, r, c = list(map(int, input().split()))
    if l < r:
        e.append((l, 'start', i))
        e.append((r, 'end', i))

e = sorted(e)

act = []
j = 0

# Loop through elements
for i in range(L):
    # Loop through events
    while j < len(e) and e[j][0] == i:
        if e[j][1] == 'start':
            act.insert(i, e[j])
        if e[j][1] == 'end':
            k = 0
            while k < len(act):
                if act[k][2] == e[j][2]:
                    del act[k]
                k += 1
        j += 1
    if len(act) == 0:
        print(0)
    else:
        act_largest_idx = act[-1]
        print(last_act[2] + 1, end=" ")
