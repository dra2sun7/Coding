import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
arr = []
max_num = 0
max_cnt = 0

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    if max(tmp) > max_num:
        max_num = max(tmp)
    arr.append(tmp)
    
def dfs(arr, n, m, depth, N):
    tmp = [(1,0),(0,1),(-1,0),(0,-1)]
    
    for x, y in tmp:
        nx, ny = n+x, m+y
        if (-1 < nx < N and -1 < ny < N) and arr[nx][ny] > depth:
            arr[nx][ny] = -1
            dfs(arr, nx, ny, depth, N)

for depth in range(0, max_num): # 1부터 max_num-1 까지의 지점이 모두 잠기게 된다.
    tmp = []
    cnt = 0
    for i in range(N):
        tmp.append(arr[i][:])
    for n in range(N):
        for m in range(N):
            if tmp[n][m] > depth:
                tmp[n][m] = -1
                dfs(tmp, n, m, depth, N)
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt


print(max_cnt)
