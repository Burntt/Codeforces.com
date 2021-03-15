
# Read data
m = int(input())
ops = []
for i in range(m):
    op = str(input()).split()
    if op[0] == 'push':
        val1, val2 = int(op[1]), int(op[2])
        ops.append((op[0], val1, val2))
    elif op[0] == 'pop':
        val3 = int(op[1])
        ops.append((op[0], val3))
    elif op[0] == 'merge':
        val4, val5 = int(op[1]), int(op[2])
        ops.append((op[0], val4, val5))
    elif op[0] == 'new':
        ops.append(op[0])

# Execute
for i in range(m):
    if op[i][0] == 'push':
        idx, x = op[i][1], op[i][2]
    elif op[i][0] == 'pop':
        idp = op[i][1]
    elif op[i][0] == 'merge':
        id1, id2 = op[i][1], op[i][2]
    elif op[i][0] == 'new':
        continue
