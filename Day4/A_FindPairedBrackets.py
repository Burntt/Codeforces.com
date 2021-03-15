def find_parenthesis(s):
    combs = {}
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            combs[stack.pop()] = i
    arr = 2 * [0] * len(combs)
    for key, value in combs.items():
        arr[key] = value
        arr[value] = key
    return arr


s = str(input())
out = find_parenthesis(s)
for i in range(len(out)):
    print(out[i], end=" ")
