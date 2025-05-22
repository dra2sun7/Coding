def dfs(arr, x, y, cnt, st):
    global answer, visited
    tmp = [(1,0),(0,1),(-1,0),(0,-1)]

    if cnt == 7:
        string = "".join(st)
        if string not in answer:
            answer.add(string)
        return
    
    for a, b in tmp:
        nx = x+a; ny = y+b
        if (-1 < nx < 4 and -1 < ny < 4):
            st.append(arr[nx][ny])
            new_index = (nx, ny, "".join(st))
            if new_index not in visited:
                visited.add(new_index)
                dfs(arr, nx, ny, cnt+1, st)
            st.pop()
    
    

T = int(input())



for i in range(1, T+1):
    global answer, visited
    answer = set()
    visited = set()
    arr = []
    for _ in range(4):
        arr.append(list(input().strip().split(" ")))
    
    for x in range(4):
        for y in range(4):
            dfs(arr, x, y, 1, [arr[x][y]])
            
    print(f"#{i} {len(answer)}")