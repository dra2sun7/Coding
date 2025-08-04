import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split(" "))
arr = []
answer = ""

for _ in range(N):
    tmp = list(sys.stdin.readline().strip())
    arr.append(tmp)


def dfs(arr, x, y):
    global answer
    if answer:
        return
    tmp = [(0,1),(1,0),(-1,0),(0,-1)]
    for a, b in tmp:
        nx = a + x; ny = y + b;
        if (-1 < nx < N and -1 < ny < M) and arr[nx][ny] == "0":
            if nx == N-1:
                answer = "YES"
                return
            arr[nx][ny] = "1"
            dfs(arr, nx, ny)

for i in range(M):
    arr[0][i] = "1"
    dfs(arr, 0, i)

if answer:
    print(answer)
else:
    print("NO")