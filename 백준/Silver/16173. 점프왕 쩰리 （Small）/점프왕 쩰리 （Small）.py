import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
arr = []
answer = ""
visited = set()

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))

def dfs(arr, x, y, move):
    global answer, visited
    if answer:
        return
    tmp = [(move,0),(0,move)]
    for a, b in tmp:
        nx = a + x; ny = b + y
        if -1 < nx < N and -1 < ny < N:
            if (nx,ny) == (N-1,N-1):
                answer = "HaruHaru"
                break
            else:
                if (nx,ny) not in visited:
                    visited.add((nx,ny))
                    dfs(arr,nx,ny,arr[nx][ny])
    

visited.add((0,0))
dfs(arr, 0, 0, arr[0][0])

if answer:
    print(answer)
else:
    print("Hing")
