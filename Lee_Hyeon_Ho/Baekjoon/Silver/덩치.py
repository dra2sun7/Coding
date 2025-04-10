import sys

N = int(sys.stdin.readline())
arr = []
rank = [1] * N

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split(" "))))
               
for i in range(N):
    for j in range(N):
        if arr[i] == arr[j]:
            continue
        
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank[i] += 1
            
rank = list(map(str, rank))
print(" ".join(rank))
