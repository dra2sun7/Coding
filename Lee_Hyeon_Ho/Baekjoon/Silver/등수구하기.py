import sys

rank = 0
tmp = 0
idx = 0
N, score, P = map(int, sys.stdin.readline().split(" "))
if N == 0:
    print(1)

else:
    arr = list(map(int, sys.stdin.readline().split(" ")))
    
    while idx < N and arr[idx] > score:
        rank += 1
        idx += 1

    if idx == N:
        if idx == P:
            # print("꼴찌인데 들어가지 못함")
            print(-1)
        else:
            # print("꼴찌인데 들어가긴 함")
            print(rank+1)
        
    else:
        # print("같은 점수가 있음")
        rank += 1
        while idx < N and arr[idx] == score:
            idx += 1
        if idx == N and idx == P:
            # print("근데 인원이 많아서 새롭게 추가 불가능")
            print(-1)
        else:
            # print("순위 안에는 들듯")
            print(rank)
            