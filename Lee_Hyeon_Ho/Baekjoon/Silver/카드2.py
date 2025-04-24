import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque([i for i in range(1,N+1)])
idx = 1

while len(arr) != 1:
    if idx == 1:
        arr.popleft()
    else:
        arr.append(arr.popleft())
        
    idx = (idx + 1)%2
    
print(arr[0])
