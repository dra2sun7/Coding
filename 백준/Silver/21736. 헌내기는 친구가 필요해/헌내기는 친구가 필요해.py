import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split(" "))
x = 0; y = 0
arr = []
cnt = 0

arr = []
for i in range(N):
    tmp = (list(sys.stdin.readline().strip()))
    if "I" in tmp:
        x = i
        y = tmp.index("I")
    
    arr.append(tmp)
    
def dfs(arr, x, y):
    global cnt
    tmp = [(0,1), (1,0), (-1,0), (0,-1)]
    for a, b in tmp:
        nx = x+a; ny = y+b
        if (-1 < nx < N and -1 < ny < M) and arr[nx][ny] != 'X':
            if arr[nx][ny] == 'P':
                cnt += 1
            arr[nx][ny] = 'X'
            dfs(arr, nx, ny)

arr[x][y] = 'X'
dfs(arr,x,y)

if cnt != 0:
    print(cnt)
else:
    print("TT")