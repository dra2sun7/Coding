def dfs(maps, x, y, cnt, dist):
    global n, m, mcnt
    if x == n and y == m:
        if dist[x][y] > cnt:
            dist[x][y] = cnt
        return
            
    print("dist 형태")
    print("#################")
    for i in dist:
        print(i)    
    print("=================")
    if dist[x][y] >= cnt:
        print("maps 형태")
        print("=================")
        for i in (maps):
            print(i)
        print("=================\n\n\n")
        dist[x][y] = cnt
        maps[x][y] = 0
        if x > 0 and maps[x-1][y] != 0:
            dfs(maps, x-1, y, cnt+1, dist)
        if y > 0 and maps[x][y-1] != 0:
            dfs(maps, x, y-1, cnt+1, dist)
        if x < n and maps[x+1][y] != 0:
            dfs(maps, x+1, y, cnt+1, dist)
        if y < m and maps[x][y+1] != 0:
            dfs(maps, x, y+1, cnt+1, dist)
        maps[x][y] = 1
        
def solution(maps):
    global n, m, mcnt
    n = len(maps) - 1
    m = len(maps[0]) - 1
    mcnt = (n+1)*(m+1)
    if maps[n-1][m] == 0 and maps[n][m-1] == 0:
        return -1
    dist = [[m*n for _ in range(m+1)] for _ in range(n+1)]
    dfs(maps, 0, 0, 1, dist)
    return dist[n][m]

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))