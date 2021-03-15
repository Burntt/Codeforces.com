

def push(stack, val):
    if len(stack) == 0:
        stack.append([val, val])
    else:
        stack.append( (val, min(val, top(stack)[1]) ) )
    return stack


def pop(stack):
    if len(stack) == 0:
        return None
    popval = stack.pop()
    return stack


def top(stack):
    if len(stack) == 0:
        return None
    else:
        return stack[-1]

def min_top(stack):
    return top(stack)[1]


n = int(input())
ops = []
for i in range(n):
    single_op = list(map(int, input().split()))
    ops.append((single_op))

stack = []
ans = []
for i in range(n):
    print(stack)
    if ops[i][0] == 1:
        stack = push(stack, ops[i][1])
    if ops[i][0] == 2:
        stack = pop(stack)
    if ops[i][0] == 3:
        ans.append(min_top(stack))

for i in range(len(ans)):
    print(ans[i])