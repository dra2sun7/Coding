import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split(" "))
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)
    
    
def dfs(V):
    visited[V] = True
    # print(f"{V+1} 위치 감염")
    for x in graph[V]:
        if not visited[x]:
            dfs(x)



def bfs():
    while queue:
        # print(queue)
        idx = queue.popleft()
        # print(f"{idx+1} 검사 시작")
        for x in graph[idx]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)
    
    
dfs(0)
print(visited.count(True) - 1)

visited = [False for _ in range(N)]
visited[0] = True
queue = deque([0])

bfs()
print(visited.count(True) - 1)
