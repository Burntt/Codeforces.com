def can(x, k, n, t_array):
    if max(t_array) > x:
        return False

    cpu_array = [0] * k
    cpu_idx = 0
    for i in range(n):
        if cpu_array[cpu_idx] + t_array[i] <= x:
            cpu_array[cpu_idx] += t_array[i]
        else:
            cpu_idx += 1
            if cpu_idx >= k:
                return False
            else:
                cpu_array[cpu_idx] += t_array[i]

    return max(cpu_array) <= x


# n = no. jobs, k = no. cpus, t_array = seconds for each job
def f(n, k, t_array):
    L = 0
    R = sum(t_array) + 1

    while R - L > 1:
        M = L + (R - L) // 2
        if can(M, k, n, t_array):
            R = M
        else:
            L = M

    return R


n, k = map(int, input().split())
t = list(map(int, input().split()))
right = f(n, k, t)
print(right)