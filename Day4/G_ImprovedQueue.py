import math


def enqueue(q, ele):
    q.append(ele)
    return q


def dequeue(q):
    val = q.pop(0)
    return q, val


def insert(q, ele):
    center = math.ceil(len(q) / 2)
    q.insert(center, ele)
    return q


def rebalance(q1, q2):
    # if append, length of q2 could exceed q1
    if len(q2) > len(q1):
        v = q2.pop(0)
        q1.append(v)
    # if insertion
    if len(q1) > len(q2) + 1:
        v = q1.pop()
        q2.insert(0, v)
    # dequeue
    if len(q1) < len(q2):
        v = q2.pop(0)
        q1.append(v)
    return q1, q2

n = int(input())
ops = []
for i in range(n):
    op = str(input()).split()
    if len(op) > 1:
        op[1] = int(op[1])
    ops.append(op)

Q1 = []
Q2 = []
dequeue_element =[]
for i in range(n):
    if ops[i][0] == '+':
        enqueue(Q2, ops[i][1])
        Q1, Q2 = rebalance(Q1, Q2)
        continue
    if ops[i][0] == '*':
        Q1.append(ops[i][1])
        Q1, Q2 = rebalance(Q1, Q2)
        continue
    if ops[i][0] == '-':
        _, val = dequeue(Q1)
        dequeue_element.append(val)
        Q1, Q2 = rebalance(Q1, Q2)
        continue

for i in range(len(dequeue_element)):
    print(dequeue_element[i])
