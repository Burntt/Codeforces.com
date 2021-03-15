s = list(str(input()).split())

stack = []

for i in range(len(s)):
    if s[i] != '+' and s[i] != '-' and s[i] != '*':
        stack.append(s[i])
    else:
        if s[i] == '+':
            val1 = int(stack.pop())
            val2 = int(stack.pop())
            res = val1 + val2
            stack.append(res)
        elif s[i] == '-':
            val1 = int(stack.pop())
            val2 = int(stack.pop())
            res = val2 - val1
            stack.append(res)
        elif s[i] == '*':
            val1 = int(stack.pop())
            val2 = int(stack.pop())
            res = val1 * val2
            stack.append(res)

print(res)