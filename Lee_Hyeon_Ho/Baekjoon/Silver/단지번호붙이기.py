import sys
from collections import deque

def dfs(arr, x, y, N):
    global cnt
    tmp = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # print(f"{x}, {y} 를 검사중")
    for a, b in tmp:
        if -1 < x+a < N and -1 < y+b < N and arr[x+a][y+b] == '1':
            arr[x+a][y+b] = '0'
            cnt += 1
            dfs(arr, x+a, y+b, N)
            
def bfs(arr, x, y, N):
    global cnt
    queue = deque([(x, y)])
    tmp = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    while queue:
        x, y = queue.popleft()
        for a, b in tmp:
            if -1 < x+a < N and -1 < y+b < N and arr[x+a][y+b] == '1':
                arr[x+a][y+b] = '0'
                cnt += 1
                queue.append((x+a, y+b))
    
global cnt
arr = []
apt = []
answer = []
N = int(sys.stdin.readline())


for _ in range(N):
    arr.append(list(sys.stdin.readline().strip()))
# print("====================")

# DFS 풀이
for x in range(N):
    for y in range(N):
        if arr[x][y] == '1':
            # print("검사 시작")
            arr[x][y] = '0'
            cnt = 1
            dfs(arr, x, y, N)
            answer.append(cnt)
            # print("검사 종료")

# BFS 풀이
for x in range(N):
    for y in range(N):
        if arr[x][y] == '1':
            arr[x][y] = '0'
            cnt = 1
            bfs(arr, x, y, N)
            answer.append(cnt)
            
            
answer.sort()
print(len(answer))
for x in answer:
    print(x)
