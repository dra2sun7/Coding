import sys

dic = dict()
T = int(sys.stdin.readline())

for _ in range(T):
    dic = dict()
    board = dict()
    cnt = dict()
    idx = dict()
    score = 0
    N = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip().split(" ")
    
    for x in arr:
        if x not in dic:
            dic[x] = 1
            board[x] = 0
            cnt[x] = 0
        else:
            dic[x] += 1
    
    for x in arr:
        if dic[x] != 6:
            continue

        else:
            score += 1
            
            if cnt[x] == 4:
                cnt[x] += 1
                idx[x] = score    
            elif cnt[x] == 5:
                continue
            else:
                board[x] += score
                cnt[x] += 1
    
    answer = 0
    answer_size = N*N
    for x in board:
        if dic[x] != 6:
            continue
        
        if board[x] < answer_size:
            answer_size = board[x]
            answer = x
        elif board[x] == answer_size:
            if idx[x] < idx[answer]:
                answer = x
    print(answer)
