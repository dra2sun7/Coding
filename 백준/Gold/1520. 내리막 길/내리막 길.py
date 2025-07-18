import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split(" "))

arr = []
dp = [[-1 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    
    arr.append(tmp)
    
def dfs(arr, dp, x, y):
    if x == N-1 and y == M-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0    
    tmp = [(1,0),(0,1),(-1,0),(0,-1)]
    
    for a, b in tmp:
        nx = x+a; ny = y+b
        if (-1 < nx < N and -1 < ny < M):
            if arr[nx][ny] < arr[x][y]:
                dp[x][y] += dfs(arr, dp, nx, ny)
        
    return dp[x][y]

print(dfs(arr, dp, 0, 0))