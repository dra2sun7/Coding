import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split(" ")))

distance = []

distance.append(arr[0])

for i in range(1,M):
    distance.append((arr[i] - arr[i-1] + 1)//2)

distance.append(N - arr[M-1])

print(max(distance))
