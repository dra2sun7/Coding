import sys
sys.setrecursionlimit(10**6)

R, C, K = map(int, sys.stdin.readline().split(" "))
arr = []
answer = 0

for _ in range(R):
    tmp = list(sys.stdin.readline().strip())
    arr.append(tmp)
    
def dfs(arr, x, y, cnt):
    global answer
    tmp = [(0,1),(1,0),(-1,0),(0,-1)]
    
    for a, b in tmp:
        nx = x + a; ny = y + b
        if -1 < nx < R and -1 < ny < C and arr[nx][ny] == ".":
            if cnt+1 == K:
                if nx == 0 and ny == C-1:
                    answer += 1
            else:
                arr[nx][ny] = "T"
                # for m in arr:
                #     print(m)
                # print("===============")
                dfs(arr, nx, ny, cnt+1)
                arr[nx][ny] = "."
                
                
arr[R-1][0] = "T"
dfs(arr, R-1, 0, 1)

print(answer)