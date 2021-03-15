s = list(str(input()))
t = list(str(input()))

len_s = len(s)
len_t = len(t)
count = 0
min_len = min(len(s), len(t))
for i in range(min_len):
    if s[len_s - 1 - i] == t[len_t - 1 - i]:
        count += 1
    else:
        break

print(len_s + len_t - count * 2)