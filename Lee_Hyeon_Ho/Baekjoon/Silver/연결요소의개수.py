import sys
sys.setrecursionlimit(10**6)

# def dfs(arr, visited, i):
#     for x in arr[i]:
#         if not visited[x]:
#             visited[x] = True
#             dfs(arr, visited, x)
    
    

# N, M = map(int, sys.stdin.readline().split(" "))
# arr = [[] for _ in range(N)]
# visited = [False for _ in range(N)]
# cnt = 0

# for _ in range(M):
#     u, v = map(int, sys.stdin.readline().split(" "))
    
#     arr[u-1].append(v-1)
#     arr[v-1].append(u-1)
    
# for i in range(N):
#     if not visited[i]:
#         visited[i] = True
#         dfs(arr, visited, i)
#         cnt += 1

# print(cnt)

N, M = map(int, sys.stdin.readline().split(" "))
arr = [[] for _ in range(N)]
visited = [False for _ in range(N)]
cnt = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split(" "))
    
    arr[u-1].append(v-1)
    arr[v-1].append(u-1)
    
for i in range(N):
    if not visited[i]:
        cnt += 1
        stack = [i]
        while stack:
            idx = stack.pop()
            visited[idx] = True
            
            for x in arr[idx]:
                if not visited[x]:
                    stack.append(x)
            
print(cnt)
    