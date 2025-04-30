import sys

idx = 0
answer = 0
N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().strip().split(" ")))
price = list(map(int, sys.stdin.readline().strip().split(" ")))

while idx <= N-2:  # 마지막에서 두번째 값까지 검사
    pr = price[idx]
    while idx <= N-3 and pr < price[idx+1]:  # 이후의 값이 
        answer += pr * distance[idx]
        idx += 1
        
    answer += pr * distance[idx]
    idx += 1
    
print(answer)
