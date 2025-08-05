import sys
from collections import defaultdict

N = int(sys.stdin.readline())
tree = defaultdict(list)

tmp = list(map(int, sys.stdin.readline().split(" ")))

for i in range(N):
    if tmp[i] == -1:
        root = i
    else:
        tree[tmp[i]].append(i)
    
# for x in tree:
#     print(f"x : {x}, tree : {tree[x]}")

T = int(sys.stdin.readline())

def dfs(tree, idx, T):
    for x in tree[idx]:
        if x == T:
            tree[idx].remove(x)
            return 0
    for x in tree[idx]:
        tmp = dfs(tree, x, T)
        if tmp == 0:
            return 0
    return 1

def check_leaf(tree, root):
    cnt = 0
    stack = [root]
    while stack:
        idx = stack.pop()
        if len(tree[idx]) == 0:
            cnt += 1
        else:
            for x in tree[idx]:
                stack.append(x)
    
    return cnt
    
if T == root:
    print(0)

else:
    dfs(tree, root, T)
    # for x in tree:
    #     print(f"x : {x}, tree : {tree[x]}")
    print(check_leaf(tree, root))
