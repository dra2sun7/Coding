import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split(" "))
tree_level = [0] * N
arr = defaultdict(list)
parents = defaultdict(list)
answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    a -= 1; b-= 1
    arr[b].append(a)
    parents[a].append(b)

def dfs(arr, i, visited):
    cnt = 1
    for x in arr[i]:
        if x not in visited:
            visited.add(x)
            cnt += dfs(arr, x, visited)
    return cnt
    

for i in range(N):
    child = dfs(arr, i, set([i]))
    parent = dfs(parents, i, set([i]))
    # print(f"{i}의 자식 수 : {child}, {i}의 부모 수 : {parent}")
    if child + parent == N + 1:
        answer += 1

print(answer)
