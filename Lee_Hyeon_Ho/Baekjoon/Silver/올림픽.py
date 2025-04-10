import sys

N, K = map(int, sys.stdin.readline().split(" "))
arr = []

for _ in range(N):
    idx, *tmp = list(map(int, sys.stdin.readline().strip().split(" ")))
    arr.append((idx, tmp))
    
arr.sort(key=lambda x: x[1], reverse="True")
rank = 1
tmp = 0

for i in range(N):
    if arr[i][0] == K:
        print(rank)
        break
    elif i < N-1:
        if arr[i+1][1] == arr[i][1]:
            tmp += 1
        else:
            rank += tmp + 1
            tmp = 0
    else:
        print(rank)
        break
