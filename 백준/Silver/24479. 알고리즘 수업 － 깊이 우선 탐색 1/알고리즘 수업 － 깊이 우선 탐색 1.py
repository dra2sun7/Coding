import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)


N, M, R = map(int, sys.stdin.readline().split(" ")) 
visited = [False] * N
arr = defaultdict(list)
answer = [0] * N
cnt = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split(" "))
    arr[u-1].append(v-1)
    arr[v-1].append(u-1)
    
for i in range(N):
    arr[i].sort()
    

def dfs(arr, R):
    global cnt
    visited[R] = True
    answer[R] = cnt
    cnt += 1
    for x in arr[R]:
        if not visited[x]:
            dfs(arr,x)
    
dfs(arr,R-1)

sys.stdout.write("\n".join(map(str, answer)) + "\n")