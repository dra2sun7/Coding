import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().split(" "))
arr = defaultdict(list)
visited = set()
answer = [-1] * N

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split(" "))
    arr[u-1].append(v-1)
    arr[v-1].append(u-1)
    
for i in arr:
    arr[i].sort()


def dfs(arr, i, cnt):
    
    for x in arr[i]:
        if len(visited) == N:
            return
        if x not in visited:
            visited.add(x)
            answer[x] = cnt
            dfs(arr, x, cnt+1)

cnt = 0
answer[R-1] = cnt
visited.add(R-1)
dfs(arr, R-1, cnt+1)

for i in answer:
    print(i)
