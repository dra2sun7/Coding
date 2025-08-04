import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split(" "))
arr = []
answer = 0

for _ in range(N):
    arr.append(list(sys.stdin.readline().strip().split(" ")))

def dfs(arr, x , y):
    tmp = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for a, b in tmp:
        nx = x + a; ny = y + b
        if -1 < nx < N and -1 < ny < M and arr[nx][ny] == "1":
            arr[nx][ny] = "0"
            dfs(arr,nx,ny)
    
    return 1

for x in range(N):
    for y in range(M):
        if arr[x][y] == "1":
            arr[x][y] = "0"
            answer += dfs(arr,x,y)
            # for m in arr:
            #     print(" ".join(m))
            # print("===================")
            # print(f"answer : {answer}")

print(answer)
