import fileinput

array = []
for key, line in enumerate(fileinput.input()):
    if key == 0:
        length, p, q = [int(x) for x in line.split()]  # read first line
    if key == 1:
        array.append([int(x) for x in line.split()])

# print([length, p, q])
# print(array[0])

array = array[0]

def rotate(l, n):
    return l[n:] + l[:n]

d_derollq = rotate(array, q)

# print(d_derollq)

D1 = d_derollq[:int(length // 2)]
D2 = d_derollq[int(length // 2):]

# print(D1)
# print(D2)


D1_derollD1 = rotate(D1, p)
D2_derollD2 = rotate(D2, p)

result = list(D1_derollD1) + list(D2_derollD2)

print(*result)