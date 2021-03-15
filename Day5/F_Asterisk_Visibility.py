def split(word):
    return [char for char in word]

def max_value(inputlist):
    return max([sublist[-1] for sublist in inputlist])

n, m = map(int, input().split())

matrix = []
for i in range(n):
    row = split( str(input()) )
    matrix.append(row)

counts = []
for i in range(n):
    counts.append([-1]*m)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '*':
            c = 1
            # row right
            for k in range(j + 1, m):
                if matrix[i][k] == '*':
                    c += 1
                else:
                    break

            # row left
            for k in range(j - 1, -1, -1):
                if matrix[i][k] == '*':
                    c += 1
                else:
                    break

            # column bottom
            for k in range(i + 1, n):
                if matrix[k][j] == '*':
                    c += 1
                else:
                    break

            # columns top
            for k in range(i - 1, - 1, -1):
                if matrix[k][j] == '*':
                    c += 1
                else:
                    break
            counts[i][j] = c
        elif matrix[i][j] == '.':
            counts[i][j] = 0

flat_count = [item for sublist in counts for item in sublist]

if len(counts) != 0:
    print(max(flat_count), flat_count.count(max(flat_count)))
