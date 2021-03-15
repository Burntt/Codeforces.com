input_str = list(str(input()))
n = len(input_str)


# input_str = '[]][[]'
# n = len(input_str)

closed_brackets = ["]", "}", ")", ">"]

l = 0
r = 0
imp = 0
for i in range(n):
    if input_str[i] == '(' or input_str[i] == '[' or input_str[i] == '{' or input_str[i] == '<':
        l += 1
    else:
        r += 1

if l != r:
    print('Impossible')
else:
    s = []
    replaces = 0
    d = {")": "(", "]": "[", "}": "{", ">": "<"}
    for i in range(n):
        if input_str[i] == '(' or input_str[i] == '[' or input_str[i] == '{' or input_str[i] == '<':
            s.append(input_str[i])
        elif len(input_str) == 0:
            imp = 1
            break
        elif len(s) != 0 and s[-1] == d[input_str[i]]:
            s.pop()
        else:
            replaces += 1
            if len(s) == 0:
                imp = 1
                break
            else:
                s.pop()
    if imp:
        print('Impossible')
    elif replaces:
        print(replaces)
    else:
        print(0)

