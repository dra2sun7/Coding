import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split(" "))
arr = defaultdict(int)
answer = 0

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    for j in range(M):
        if tmp[j] != 0:
            arr[(i,j)] = tmp[j]

def check_size(arr):
    stack = [next(iter(arr))]
    visited = set([stack[0]])
    tmp = [(0,1),(1,0),(-1,0),(0,-1)]
    while stack:
        x, y = stack.pop()
        for a, b in tmp:
            nx = x+a; ny = y+b
            if -1 < nx < N and -1 < ny < M and (nx,ny) in arr and (nx,ny) not in visited:
                visited.add((nx,ny))
                stack.append((nx,ny))
    
    if len(visited) != len(arr):
        return True
    return False

def melting(arr):
    k = []
    tmp = [(0,1),(1,0),(-1,0),(0,-1)]
    for x, y in arr:
        cnt = 0
        for a, b in tmp:
            nx = x+a; ny = y+b
            if -1 < nx < N and -1 < ny < M and (nx,ny) not in arr:
                cnt += 1
        arr[(x,y)] -= cnt
    
    for x in arr:
        if arr[x] <= 0:
            k.append(x)
    
    for x in k:
        arr.pop(x)

while True:
    if len(arr) == 0:
        answer = 0
        break
    elif check_size(arr):
        break
    answer += 1
    
    melting(arr)
    
    # for x in arr:
    #     print(f"x : {x}, height : {arr[x]}")

print(answer)