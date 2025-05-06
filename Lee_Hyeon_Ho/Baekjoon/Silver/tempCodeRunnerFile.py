import sys

N = int(sys.stdin.readline())
arr = [[] for _ in range(N)]
depth = [0 for _ in range(N)]
parents = [0 for _ in range(N)]
visited = [False for _ in range(N)]
visited[0] = True


for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().split(" "))
    arr[x-1].append(y-1)
    arr[y-1].append(x-1)
    

def dfs(arr, visited, parents, depth, index, size):
    nodes = arr[index]
    depth[index] = size

    for x in nodes:
        if not visited[x]:
            visited[x] = True
            parents[x] = index+1
            dfs(arr, visited, parents, depth, x, size+1)
    
dfs(arr, visited, parents, depth, 0, 1)
for i in range(1,N):
    print(parents[i])

