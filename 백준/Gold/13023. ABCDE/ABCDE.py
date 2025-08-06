import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split(" "))
visited = [False] * N
arr = defaultdict(list)
answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    
    arr[b].append(a)
    arr[a].append(b)

def dfs(arr, idx, visited, cnt):
    for i in arr[idx]:
        if not visited[i]:
            if cnt == 3:
                return 1
            visited[i] = True
            if dfs(arr, i, visited, cnt+1) == 1:
                return 1
            visited[i] = False
    
for i in range(N):
    visited[i] = True
    if dfs(arr, i, visited, 0) == 1:
        answer = 1
        break
    visited[i] = False
    
print(answer)
