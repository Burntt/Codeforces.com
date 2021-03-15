inputstr = str(input())

n = len(inputstr)

count = dict()
Re = []

for i in range(n):
    a = inputstr[i]
    if a in count:
        count[a] += 1
    else:
        count[a] = 1

i = 'a'
while i <= 'z':
    if i in count and count[i] % 2 != 0:
        Re += i
    i = chr(ord(i) + 1)
l = len(Re)
j = 0

for i in range(l - 1, (l // 2) - 1, -1):
    if Re[i] in count:
        count[Re[i]] -= 1
    else:
        count[Re[i]] = -1
    Re[i] = Re[j]
    if Re[j] in count:
        count[Re[j]] += 1
    else:
        count[Re[j]] = 1
    j += 1

left, mid, right = "", "", ""

i = 'a'
while i <= 'z':
    if i in count:
        if count[i] % 2 == 0:
            j = 0
            while j < count[i] // 2:
                left += i
                j += 1
        else:
            j = 0
            while j < (count[i] - 1) // 2:
                left += i
                j += 1
            mid += i
    i = chr(ord(i) + 1)

right = left
right = ''.join(reversed(right))
res = left + mid + right
print(res)