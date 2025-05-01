import sys
sys.setrecursionlimit(10**6)
# 재귀가 들어갈 수 있는 한도는 기본적으로 1000개, 이를 늘리는 방법이 setrecursionlimit

def dfs(arr, N, M, x, y):
    tmp = [(1,0),(0,1),(-1,0),(0,-1)]
    
    for a, b in tmp:
        if (-1<x+a<N and -1<y+b<M) and arr[x+a][y+b] == 1:
            arr[x+a][y+b] = 0
            # for k in arr:
            #     print(k)
            # print("================")
            dfs(arr, N, M, x+a, y+b)

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split(" "))
    # visited = [False for _ in range(K)]
    arr = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split(" "))
        arr[x][y] = 1
        
    # for k in arr:
    #     print(k)
    # print("================")

    for x in range(N):
        for y in range(M):
            if arr[x][y] == 1:
                cnt += 1
                arr[x][y] = 0
                # for k in arr:
                #     print(k)
                # print("================")
                dfs(arr, N, M, x, y)
    print(cnt)
