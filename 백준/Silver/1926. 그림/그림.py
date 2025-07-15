import sys
sys.setrecursionlimit(10**6)

def dfs(arr, x, y, n, m):
    global max_cnt, cnt
    tmp = [(1,0), (0,1), (-1,0), (0,-1)]
    
    for i,j in tmp:
        nx = i+x
        ny = j+y
        
        if (-1 < nx < n and -1 < ny < m) and arr[nx][ny] == 1:
            arr[nx][ny] = 0
            cnt += 1
            dfs(arr, nx, ny, n, m)

n, m = map(int, sys.stdin.readline().split(" "))
arr = []
answer = 0
max_cnt = 0

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    arr.append(tmp)

for x in range(n):
    for y in range(m):
        if arr[x][y] == 1:
            cnt = 1
            arr[x][y] = 0
            answer += 1
            dfs(arr, x, y, n, m)
            
            if cnt > max_cnt:
                max_cnt = cnt
                
print(answer)
print(max_cnt)