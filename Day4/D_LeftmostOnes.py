from collections import deque

def windowedones(n, m, str):
    first_ones = [-1] * (n - m + 1)
    queue = deque()

    # if windows size is greater than string
    if n < m:
        return [-1]

    # add all locations of ones in first window to queue
    for i in range(m):
        if str[i] == '1':
            queue.append(i)

    # if there are ones in queue, set location of first one
    # to first value in queue
    # else there are no ones in the str, therefore impossible
    if len(queue) > 0:
        first_ones[0] = queue[0]
    else:
        first_ones[0] = -1

    # Loop through all possible windows of size m in the str
    for i in range(1, n - m + 1):
        # if the first character of this window equals one pop the index from the que
        if str[i - 1] == '1':
            queue.popleft()
        # if the first character of the next window equals one add it to the que
        if str[i + m - 1] == '1':
            queue.append(i + m - 1)
        # if the que has elements, the index corresponding to the first one in the window
        # equals the first element in the que minus the current index of the string
        if len(queue) > 0:
            first_ones[i] = queue[0] - i
    return first_ones


t = int(input())
test_cases = []
for i in range(t):
    n, m = map(int, input().split())
    binstr = str(input())
    test_cases.append((n, m, binstr))

for i in range(len(test_cases)):
    n, m, binstr = test_cases[i]
    print( *windowedones(n, m, binstr) , sep = " ")
#
# i = 2
# n, m, binstr = test_cases[i]
# print( windowedones(n, m, binstr) )