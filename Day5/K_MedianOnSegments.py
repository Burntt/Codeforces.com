# import math
#
# n, m = map(int, input().split())
# p = list(map(int, input().split()))
#
# for i in range(n):
#     if p[i] == m:
#         pos = i
#
# cnt = 0
# for i in range(n):
#     if p[i] > m:
#         cnt += 1
#     if p[i] < m:
#         cnt -= 1
#
# pairs = []
# for i in range(n):
#     for j in range(n):
#         slice = sorted( p[i:j] )
#
#         if len(slice) % 2:
#
#         if len(slice) > 0:
#             center = int( math.floor( len(slice) / 2 ) )
#             if slice[center] == m:
#                 pairs.append((i,j))
#
# print(pairs)
#
# for i in range(len(pairs)):
#     l, r = pairs[i]
#     print(p[l:r])
