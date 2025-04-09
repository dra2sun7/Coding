import sys
from collections import deque

N = int(sys.stdin.readline())
arr = []
answer = []
idx = 0

for i in range(N):
    arr.append(sys.stdin.readline().strip())

while arr[idx] != "KBS1":
    idx += 1
    answer.append("1")
    
while arr[0] != "KBS1":
    tmp = arr[idx]
    arr[idx] = arr[idx-1]
    arr[idx-1] = tmp
    
    idx -= 1
    answer.append("4")

while arr[idx] != "KBS2":
    idx += 1
    answer.append("1")

while arr[1] != "KBS2":
    tmp = arr[idx]
    arr[idx] = arr[idx-1]
    arr[idx-1] = tmp
    
    idx -= 1
    answer.append("4")

print("".join(answer))