import sys

def dfs(arr, stack, N, S):
    tmp = [(1,0),(0,1),(-1,0),(0,-1)]
    while stack:
        x, y = stack.pop()

        for a, b in tmp:
            nx = x+a; ny = y+b
            
            if (-1<nx<N and -1<ny<N) and arr[nx][ny] == S:
                arr[nx][ny] = 'T'
                stack.append((nx, ny))
                
def dfs_RG(arr, stack, N):
    tmp = [(1,0),(0,1),(-1,0),(0,-1)]
    while stack:
        x, y = stack.pop()

        for a, b in tmp:
            nx = x+a; ny = y+b
            
            if (-1<nx<N and -1<ny<N) and (arr[nx][ny] == "R" or arr[nx][ny] == "G"):
                arr[nx][ny] = 'T'
                stack.append((nx, ny))
    
N = int(sys.stdin.readline())
l = []
cnt = 0

for _ in range(N):
    l.append(list(sys.stdin.readline().strip()))

arr = [x[:] for x in l]
# for p in arr:
#     print(p)
# print("=========================")

# print("히디님의 경우")
for x in range(N):
    for y in range(N):
        if arr[x][y] != 'T':
            dfs(arr, [(x, y)], N, arr[x][y])
            cnt += 1
            # for p in arr:
            #     print(p)
            # print("=========================")
            
print(cnt, end=" ")
# print(cnt)   
arr = [x[:] for x in l]
cnt = 0

# for p in arr:
#     print(p)
# print("=========================")
# print("진돌님의 경우")
for x in range(N):
    for y in range(N):
        if arr[x][y] != 'T':
            if arr[x][y] == "B":
                dfs(arr, [(x, y)], N, arr[x][y])
            else:
                dfs_RG(arr, [(x, y)], N)
            cnt += 1
            # for p in arr:
            #     print(p)
            # print("=========================")
            
print(cnt)
