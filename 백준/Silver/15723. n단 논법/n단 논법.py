import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

arr = defaultdict(list)
answer = []

N = int(sys.stdin.readline())

for _ in range(N):
    tmp = list(sys.stdin.readline().strip().split(" "))
    arr[tmp[0]].append(tmp[2])

M = int(sys.stdin.readline())

def dfs(arr, start, end):
    global T_F
    if T_F:
        return
    for x in arr[start]:
        if x == end:
            T_F = "T"
        else:
            dfs(arr, x, end)

for _ in range(M):
    T_F = ""
    tmp = list(sys.stdin.readline().strip().split(" "))
    dfs(arr, tmp[0], tmp[2])
    if T_F:
        answer.append(T_F)
    else:
        answer.append("F")

print("\n".join(answer))
