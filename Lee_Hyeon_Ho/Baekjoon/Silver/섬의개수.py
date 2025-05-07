import sys
sys.setrecursionlimit(10**6)

def dfs(arr, i, j, w, h):
    tmp = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        for n, m in tmp:
            nx = x+n; ny = y+m
            if -1 < nx < h and -1 < ny < w and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                stack.append((nx,ny))
        

w, h = map(int, sys.stdin.readline().split(" "))

while w+h > 1:
    arr = []
    cnt = 0
    
    for _ in range(h):
        tmp = list(map(int, sys.stdin.readline().split(" ")))
        arr.append(tmp)
        
    # for p in arr:
    #         print(p)
    # print("+++++++++++++++++++++++++++++")
        
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                arr[i][j] = 0
                cnt += 1
                dfs(arr, i, j, w, h)
        # for p in arr:
        #     print(p)
        # print("+++++++++++++++++++++++++++++")
    print(cnt)
    w, h = map(int, sys.stdin.readline().split(" "))
    