from collections import deque

def make_blank(board, queue, a, b):
    global n
    arr = [(0, 0)]
    
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        x, y = queue.popleft()
        board[x][y] = 1
        for i, j in move:
            if  (0 <= x+i < n) and (0 <= y+j < n) and (board[x+i][y+j] == 0):
                arr.append((x+i-a, y+j-b))
                queue.append((x+i, y+j))
        
    return arr

def make_puzzle(board, queue, a, b):
    global n
    arr = [(0, 0)]
    
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        x, y = queue.popleft()
        board[x][y] = 0
        for i, j in move:
            if  (0 <= x+i < n) and (0 <= y+j < n) and (board[x+i][y+j] == 1):
                arr.append((x+i-a, y+j-b))
                queue.append((x+i, y+j))
        
    return arr

def rotate(puzzle):
    xm, ym = None, None
    tmp = []
    arr = []
    for x, y in puzzle:
        tmp.append((y, -x))
        if xm == None:
            xm = y
            ym = -x
        else:
            if xm > y:
                xm = y
                ym = -x
            elif xm == y and ym > -x:
                ym = -x
        
    # print(f"tmp : {tmp}, xm : {xm}, ym : {ym}")
    for x, y in tmp:
        arr.append((x-xm, y-ym))
            
    return arr

def dfs(blank, puzzle, cnt):
    global mcnt
    
    # for b in blank:
        
    
    

def solution(game_board, table):
    global mcnt, n
    mcnt = 0
    n = len(game_board)
    blank = []
    puzzle = []
    
    board = [[game_board[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                blank.append(make_blank(board, deque([(i, j)]), i, j))
    
    board = [[table[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                puzzle.append(make_puzzle(board, deque([(i, j)]), i, j))

# 90도 회전 : (x , y) -> (y, -x)

    for x in game_board:
        print(x)
    print("===============")
    for x in table:
        print(x)
    
    
    return 0