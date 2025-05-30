M, N, K = map(int, input().split(" "))

arr = [[0 for _ in range(N)] for _ in range(M)]
answer = []
cnt = 0

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split(" "))
    x, y = x1, y1
    while x < x2:
        while y < y2:
            arr[x][y] = 1
            y += 1
        x += 1; y = y1


def dfs(stack):
    tmp = [(1,0),(0,1),(-1,0),(0,-1)]
    sum = 1
    
    while stack:
        x, y = stack.pop()
        for a, b in tmp:
            nx = x+a; ny = y+b
            if -1 < nx < M and -1 < ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                sum += 1
                stack.append((nx,ny))
    
    answer.append(sum)
    
for x in range(M):
    for y in range(N):
        if arr[x][y] == 0:
            cnt += 1
            arr[x][y] = 1
            dfs([(x, y)])
            
answer.sort()

print(cnt)
print(" ".join(list(map(str, answer))))