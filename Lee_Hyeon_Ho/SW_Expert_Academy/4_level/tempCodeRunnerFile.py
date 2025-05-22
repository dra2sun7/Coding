from collections import deque

T = int(input())

for i in range(T):
    N = int(input())
    arr = []
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    
    for _ in range(N):
        arr.append(list(map(int, list(input()))))
    

    queue = deque([(0,0)])

    while queue:
        x, y = queue.popleft()
        tmp = [(1,0),(0,1)]
        
        for a, b in tmp:
            nx = x+a; ny = y+b
            if -1 < nx < N and -1 < ny < N:
                queue.append((nx,ny))
                if (visited[nx][ny] == -1) or (visited[x][y] + arr[nx][ny] < visited[nx][ny]):
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
        
    print(f"#{i+1} {visited[N-1][N-1]}")