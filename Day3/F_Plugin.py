

def push(stack, val):
    if len(stack) == 0:
        stack.append(val)
    else:
        stack.append(val)
    return stack

def pop(stack):
    if len(stack) == 0:
        return None
    stack.pop()
    return stack

def top(stack):
    if len(stack) == 0:
        return None
    else:
        return stack[-1]

s = list( str(input()) )

#print(s)

stack = []
stack.append(s[0])
ans = []
#print('Starting stack', stack)
for i in range(1, len(s)):
    # print(stack)
    # print('--------')
    # print('s[i] =', s[i])
    # print('top(stack) =',  top(stack))
    # print('equals?:', top(stack) == s[i])
    if top(stack) == s[i]:
        #print('equal char, popping')
        pop(stack)
    else:
        #print('nonequal char, pushing')
        push(stack, s[i])

print(''.join(stack))



