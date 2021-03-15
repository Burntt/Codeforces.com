from collections import defaultdict

n, a, b = list(map(int, input().split()))
adj_list = defaultdict(lambda: [])
for i in range(1, n + 1):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1:
            adj_list[i].append(j + 1)


def dfs(v, p, visited, parents, adj_list):
    parents[v] = p
    visited[v] = 1
    for i in range(len(adj_list[v])):
        if visited[adj_list[v][i]] == 0:
            visited, parents = dfs(adj_list[v][i], v, visited, parents, adj_list)
    return visited, parents


def get_path_to(v, parents):
    path = []
    if parents[v] == -1:
        return None
    while parents[v] != v:
        path.append(v)
        v = parents[v]
    path.append(v)
    return path[::-1]


parents = [-1] * (n + 1)
visited = [0] * (n + 1)

visited, parents = dfs(a, a, visited, parents, adj_list)

path = get_path_to(b, parents)

if path is None:
    print('-1')
else:
    print(len(path) - 1)
    print(*path)