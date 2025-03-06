from collections import deque

def solution(maps):
    n = len(maps) - 1
    m = len(maps[0]) - 1
    mcnt = -1
    
    queue = deque([(0,0,1)])

    while queue:
        x, y, cnt = queue.popleft()
        

        if x == n and y == m:
            if mcnt > cnt or mcnt == -1:
                return cnt
                
        if x-1 != -1 and maps[x-1][y] == 1:
            maps[x-1][y] = 0
            tmp = (x-1, y, cnt+1)
            queue.append(tmp)
        if x != n and maps[x+1][y] == 1:
            maps[x+1][y] = 0
            tmp = (x+1, y, cnt+1)
            queue.append(tmp)
        if y-1 != -1 and maps[x][y-1] == 1:
            maps[x][y-1] = 0
            tmp = (x, y-1, cnt+1)
            queue.append(tmp)
        if y != m and maps[x][y+1] == 1:
            maps[x][y+1] = 0
            tmp = (x, y+1, cnt+1)
            queue.append(tmp)
    
    return mcnt