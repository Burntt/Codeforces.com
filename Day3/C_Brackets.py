open_brackets = ["[", "{", "(", "<"]
closed_brackets = ["]", "}", ")", ">"]


def balancedornah(input_str):
    stack = []
    idx_stack = []
    matching_indexes = []
    ans = ' '
    for i in input_str:
        idx = input_str.index(i)
        if i in open_brackets:
            stack.append(i)
            idx_stack.append(idx)
        elif i in closed_brackets:
            pos = closed_brackets.index(i)
            if (len(stack) > 0) and (open_brackets[pos] == stack[len(stack) - 1]):
                stack.pop()
                matching_indexes.append([idx_stack.pop(), idx])
            else:
                ans = "NO"
    if len(stack) == 0:
        ans = "YES"
    else:
        ans = "NO"
    return ans, matching_indexes


input_str = str(input())
res, matching_indexes = balancedornah(input_str)
print(res)