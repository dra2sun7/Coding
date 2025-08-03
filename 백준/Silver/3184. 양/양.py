import sys
sys.setrecursionlimit(10**6)

R, C = map(int, sys.stdin.readline().split(" "))
arr = []
answer = [0, 0]

for _ in range(R):
    tmp = list(sys.stdin.readline().strip())
    arr.append(tmp)

def dfs(arr, x, y):
    global O_cnt, V_cnt
    tmp = [(0,1),(1,0),(-1,0),(0,-1)]
    
    for a, b in tmp:
        nx = a+x; ny = b+y
        
        if (-1 < nx < R and -1 < ny < C) and arr[nx][ny] != "#":
            if arr[nx][ny] == "o":
                O_cnt += 1
            elif arr[nx][ny] == "v":
                V_cnt += 1
            arr[nx][ny] = "#"
            dfs(arr, nx, ny)

for x in range(R):
    for y in range(C):        
        O_cnt = 0
        V_cnt = 0
        if arr[x][y] != "#":
            if arr[x][y] == "o":
                O_cnt += 1
            elif arr[x][y] == "v":
                V_cnt += 1
            arr[x][y] = "#"
            dfs(arr, x, y)
        if O_cnt > V_cnt:
            answer[0] += O_cnt
        else:
            answer[1] += V_cnt

print(answer[0], answer[1])