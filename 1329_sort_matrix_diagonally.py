def diagonal_sort(mat):
    m, n = len(mat), len(mat[0])
    d = {}
    for i in range(m):
        for j in range(n):
            if (i - j) in d:
                d[i - j].append(mat[i][j])
            else:
                d[i - j] = [mat[i][j]]
    for k in d:
        d[k].sort(reverse=True)
    for i in range(m):
        for j in range(n):
            mat[i][j] = d[i - j].pop()
    return mat

print(diagonal_sort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
