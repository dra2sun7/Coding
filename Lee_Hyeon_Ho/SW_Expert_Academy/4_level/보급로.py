from collections import deque

T = int(input())

for i in range(T):
    N = int(input())
    arr = []
    visited = [[float('inf') for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    
    for _ in range(N):
        arr.append(list(map(int, list(input()))))
    

    queue = deque([(0,0,0)])

    while queue:
        x, y, cost = queue.popleft()
    
        if visited[x][y] < cost:
            continue
        
        tmp = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for a, b in tmp:
            nx = x+a; ny = y+b
            
            if -1 < nx < N and -1 < ny < N:
                new_cost = cost + arr[nx][ny]
                if new_cost < visited[nx][ny]:
                    visited[nx][ny] = new_cost
                    queue.append((nx,ny,new_cost))
        
    print(f"#{i+1} {visited[N-1][N-1]}")