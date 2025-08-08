import sys


N = int(sys.stdin.readline())
arr = []
answer = set()
pp = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()) - 1)

# print("=========")

def dfs(arr, i, visited):
    stack = [i]
    dic1 = set()
    dic2 = set()
    while stack:
        idx = stack.pop()
        if arr[idx] >= N:
            return 0
        dic1.add(idx)
        dic2.add(arr[idx])
        if dic1 == dic2:
            return dic1
        
        if arr[idx] not in visited:
            visited.add(arr[idx])
            stack.append(arr[idx])
            
    return 0
        
for i in range(N):
    visited = set([i])
    visited.update(answer)
    t = dfs(arr, i, visited)
    if t != 0:
        answer.update(t)

print(len(answer))

answer = list(answer)
answer.sort()
for i in answer:
    print(i+1)
