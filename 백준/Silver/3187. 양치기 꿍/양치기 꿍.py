import sys
sys.setrecursionlimit(10**6)

R, C = map(int, sys.stdin.readline().split(" "))
arr = []
answer = [0, 0]

for _ in range(R):
    arr.append(list(sys.stdin.readline().strip()))

def dfs(arr, x, y):
    global v_cnt, k_cnt
    tmp = [(0,1),(1,0),(0,-1),(-1,0)]
    for a, b in tmp:
        nx = x + a; ny = y + b
        if -1 < nx < R and -1 < ny < C and arr[nx][ny] != "#":
            if arr[nx][ny] == "v":
                v_cnt += 1
            elif arr[nx][ny] == "k":
                k_cnt += 1
            arr[nx][ny] = "#"
            dfs(arr, nx, ny)

for x in range(R):
    for y in range(C):
        if arr[x][y] != "#":
            v_cnt = 0; k_cnt = 0
            if arr[x][y] == "v":
                v_cnt += 1
            elif arr[x][y] == "k":
                k_cnt += 1
            arr[x][y] = "#"
            dfs(arr,x,y)
            
            if k_cnt > v_cnt:
                answer[0] += k_cnt
            else:
                answer[1] += v_cnt

print(answer[0], answer[1])
