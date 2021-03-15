n = int(input())

ops = []
for i in range(n):
    ops.append(list(str(input()).split()))

s1 = []
s2 = []
hist = []

def enQ(ele):
    s1.append(ele)
    hist.append('1' + ' + ' + str(ops[i][1]))

def deQ():
    if len(s2) == 0:
        if len(s1) == 0:
            return 'Cannot deque, s1 empty'
        while len(s1) > 0:
            val = s1.pop()
            hist.append('1' + ' - ' + str(val))
            s2.append(val)
            hist.append('2' + ' + ' + str(val))

    val1 = s2[-1]
    hist.append('2' + ' - ' + str(val1))
    return s2.pop()


for i in range(n):
    if ops[i][0] == '+':
        enQ(ops[i][1])
    if ops[i][0] == '-':
        deQ()

for i in range(len(hist)):
    print(hist[i])