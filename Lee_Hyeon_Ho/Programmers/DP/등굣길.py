def solution(m, n, puddles):
    arr = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        if [1, i+1] in puddles:
            break
        arr[i][0] = 1
    for i in range(m):
        if [i+1, 1] in puddles:
            break
        arr[0][i] = 1
        
    
    for y in range(1, m):
        for x in range(1, n):
            if [y+1, x+1] in puddles:
                continue
            arr[x][y] = arr[x-1][y] + arr[x][y-1]
    
    return arr[n-1][m-1] % 1000000007