def find_root(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

def solution(n, computers):
    parent = [i for i in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                root_i = find_root(parent, i)
                root_j = find_root(parent, j)
                parent[root_j] = parent[root_i]
                
    
    for i in range(n):
        if parent[i] == i:
            cnt += 1
    
    return cnt
