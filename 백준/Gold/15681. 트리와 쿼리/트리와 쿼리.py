import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

N, R, Q = map(int, sys.stdin.readline().split(" "))
arr = defaultdict(set)
level = [0] * N
quiz = []

for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split(" "))
    
    U -= 1; V -= 1
    arr[U].add(V)
    arr[V].add(U)

for _ in range(Q):
    quiz.append(int(sys.stdin.readline()) - 1)

def leveling(arr, i):
    queue = deque([i])
    visited = set([i])
    while queue:
        idx = queue.popleft()
        tmp = set()
        for x in arr[idx]:
            if x not in visited:
                tmp.add(x)
                visited.add(x)
                queue.append(x)
        arr[idx] = tmp

leveling(arr, R-1)

def dfs(arr, i):
    global level
    cnt = 1
    for x in arr[i]:
        cnt += dfs(arr, x)

    level[i] = cnt
    return cnt

dfs(arr, R-1)

for q in quiz:
    print(level[q])