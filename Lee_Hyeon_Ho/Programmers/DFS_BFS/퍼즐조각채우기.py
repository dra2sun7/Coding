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
        
    for x, y in tmp:
        arr.append((x-xm, y-ym))
            
    return arr

def can_fit(blank, puzzle):
    b_set = set(blank)
    for _ in range(4):  # 4번 회전하면서 확인
        p_set = set(puzzle)
        if p_set.issubset(b_set):
            return True
        puzzle = rotate(puzzle)
    return False


def backtrack(used, count):
    global mcnt, blank, puzzle

    # 최댓값 업데이트
    mcnt = max(mcnt, count)

    for i in range(len(blank)):
        for j in range(len(puzzle)):
            if used[j]:  # 이미 사용한 퍼즐이면 건너뜀
                continue
            if can_fit(blank[i], puzzle[j]):  # 퍼즐이 빈칸에 맞으면
                used[j] = True
                backtrack(used, count + len(puzzle[j]))  # 퍼즐을 놓고 다음 단계로
                used[j] = False  # 원래 상태로 되돌리기 (백트래킹)

def solution(game_board, table):
    global mcnt, blank, puzzle, n
    mcnt = 0
    n = len(game_board)
    blank = []
    puzzle = []
    
    board = [[game_board[i][j] for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                blank.append(make_blank(board, deque([(i, j)]), i, j))
    
    board = [[table[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                puzzle.append(make_puzzle(board, deque([(i, j)]), i, j))

    used = [False] * len(puzzle)  # 퍼즐 사용 여부
    
    backtrack(used, 0)

    
    return 0