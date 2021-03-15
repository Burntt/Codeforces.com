n = int(input())

ops = []
for i in range(n):
    single_op = list( map(int, input().split()) )
    ops.append((single_op))


def push(stack, val):
    stack.append(val)
    return stack


def pop(stack):
    if len(stack) == 0:
        return None
    val = stack[-1]
    stack.pop()
    return stack, val


stack = []
for i in range(n):
    if ops[i][0] == 1:
        stack = push(stack, ops[i][1])
    if ops[i][0] == 2:
        stack, val = pop(stack)