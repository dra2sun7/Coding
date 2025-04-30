import sys
from collections import deque

N,M,V = map(int, sys.stdin.readline().split(" "))
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]
answer = []

for _ in range(M):   # 인접 그래프 만들기
    x, y = map(int, sys.stdin.readline().split(" "))
    graph[x-1].append(y)
    graph[y-1].append(x)

for i in range(N):   # 정렬을 통해 숫자가 작은 값부터 탐색
    graph[i].sort()

def dfs(V):
    visited[V-1] = True
    answer.append(V)
    # print(f"{V} 위치 방문")
    for x in graph[V-1]:
        if not visited[x-1]:
            dfs(x)
            
def bfs():
    while queue:
        # print(queue)
        x = queue.popleft()
        if visited[x-1] == False:
            visited[x-1] = True
            answer.append(x)
            for y in graph[x-1]:
                queue.append(y)

dfs(V)
print(" ".join(map(str, answer)))

visited = [False for _ in range(N)]
answer = [V]
queue = deque(graph[V-1])
visited[V-1] = True
# print(graph)
# print("====================")

bfs()
print(" ".join(map(str, answer)))