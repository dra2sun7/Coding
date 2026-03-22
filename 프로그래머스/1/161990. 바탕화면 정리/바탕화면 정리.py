def solution(wallpaper):
    lux, luy, rdx, rdy = -1, -1, -1, -1
    n = len(wallpaper)
    m = len(wallpaper[0])
    tmp = 0
    for i in range(n):
        for j in range(m):
            if tmp == 0:
                if wallpaper[i][j] == '#':
                    lux = i
                    rdx = i+1
                    tmp = 1
                    break
            else:
                if wallpaper[i][j] == '#':
                    rdx = i+1
    tmp = 0
    for j in range(m):
        for i in range(n):
            if tmp == 0:
                if wallpaper[i][j] == '#':
                    luy = j
                    rdy= j+1
                    tmp = 1
                    break
            else:
                if wallpaper[i][j] == '#':
                    rdy = j+1
            
    return [lux, luy, rdx, rdy]