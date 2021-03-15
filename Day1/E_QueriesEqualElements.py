n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
for x in b:
    l = -1
    r = n
    while r > l + 1:
        mid = (l + r) // 2
        if a[mid] <= x:
            l = mid
        else:
            r = mid
    print(r, end=" ")