import sys
from collections import defaultdict, deque


n = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split(" "))
p1 -= 1; p2 -= 1
m = int(sys.stdin.readline())
tree = defaultdict(lambda: -1)
level = [1 for _ in range(n)]
answer = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    a -= 1; b -= 1
    # 부모를 가리키는 tree 구현
    tree[b] = a
    level[b] = level[a] + 1

# for x in tree:
#     print(f"x : {x}, 부모 노드 : {tree[x]}")

# print(f"level : {level}")

if level[p1] > level[p2]:
    while level[p1] != level[p2]:
        answer += 1
        p1 = tree[p1]
        
elif level[p1] < level[p2]:
    while level[p1] != level[p2]:
        answer += 1
        p2 = tree[p2]
        
# print(f"p1 : {p1}, p2 : {p2}")
# print(f"answer : {answer}")

if p1 == p2:
    print(answer)
else:
    while (p1 != -1) and (p2 != -1):
        p1 = tree[p1]
        p2 = tree[p2]
        answer += 2
        
        if p1 == p2:
            break

    if p1 == -1:
        print(-1)
    else:
        print(answer)
