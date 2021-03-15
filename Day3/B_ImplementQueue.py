n = int(input())

ops = []
for i in range(n):
    single_op = str(input()).split()
    if len(single_op) > 1:
        single_op[1] = int(single_op[1])
    ops.append((single_op))

def add(queue, val):
    queue.insert(0,val)
    return queue


def pop(queue):
    if len(queue) == 0:
        return None
    val = queue[-1]
    queue.pop()
    return queue, val


queue = []
popped_ele = []
for i in range(n):
    # print('=========================')
    # print('Loop', i, 'queue is :', queue)
    # print(ops[i])
    # print(ops[i][0] == '+')
    if ops[i][0] == '+':
        queue = add(queue, ops[i][-1])
        #print('value added', ops[i][-1])
    if ops[i][0] == '-':
        queue, val = pop(queue)
        popped_ele.append(val)
    # print(queue)

for i in range(len(popped_ele)):
    print(popped_ele[i])