import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split(" "))
arr = []
answer = 0

for _ in range(R):
    arr.append(list(sys.stdin.readline().strip()))

# def dfs(x, y, visit, cnt):
#     global answer
#     tmp = [(1,0),(0,1),(-1,0),(0,-1)]
    
#     for a, b in tmp:
#         nx = x+a; ny = y+b
#         if (-1 < nx < R and -1 < ny < C):
#             ch = (ord(arr[nx][ny]) - ord('A'))
#             if not (visit & 1 << ch):
#                 dfs(nx, ny, visit | (1 << ch), cnt+1)
            
#     if answer < cnt:
#         answer = cnt
        
# dfs(0, 0, 1 << (ord(arr[0][0]) - ord('A')), 1)
# print(answer)

queue = deque([(0,0,1 << (ord(arr[0][0]) - ord('A')), 1)])
visited = set([(0,0,1 << (ord(arr[0][0]) - ord('A')))])

while queue:
    x, y, bitmask, cnt = queue.popleft()
    tmp = [(1,0),(0,1),(-1,0),(0,-1)]
    answer = max(cnt, answer)
    
    for a, b in tmp:
        nx = x+a; ny = y+b
        if -1 < nx < R and -1 < ny < C:
            ch = ord(arr[nx][ny]) - ord('A')
            mask = 1 << ch
            if not (bitmask & mask):
                new_state = (nx, ny, bitmask | mask)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((nx, ny, bitmask | mask, cnt + 1))
            
                
print(answer)
