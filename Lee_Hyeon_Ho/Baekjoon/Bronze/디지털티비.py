import sys
from collections import deque
def solution1():
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

def up_input(arr, idx, answer, queue):
    queue.append([arr[:], idx-1, answer + "2"])
    
    arr[idx], arr[idx-1] = arr[idx-1], arr[idx]
    queue.append([arr[:], idx-1, answer + "4"])
    arr[idx], arr[idx-1] = arr[idx-1], arr[idx]
    
def down_input(arr, idx, answer, queue):
    queue.append([arr[:], idx+1, answer + "1"])
    
    arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
    queue.append([arr[:], idx+1, answer + "3"])
    arr[idx], arr[idx+1] = arr[idx+1], arr[idx]

# BFS 해결
def bfs_solution():
    N = int(sys.stdin.readline())
    queue = deque()
    arr = []
    
    for _ in range(N):
        arr.append(sys.stdin.readline().strip())
    
    queue.append([arr[:], 0, ""])
    # Tuple은 해시가 가능해서 set() 형태에 넣을 수 있음
    visited = set()
    
    
    while queue:
        # print(queue)
        arr, idx, answer = queue.popleft()
        # print("현재 탐색 중인 상태")
        # print(f"arr : {arr}")
        # print(f"idx : {idx}")
        # print(f"answer : {answer}")
        if arr[0] == "KBS1" and arr[1] == "KBS2":
            return answer
        
        elif ("".join(arr), idx) in visited:
            continue
            
        visited.add(("".join(arr), idx))
        
        if idx == N-1:
            up_input(arr, idx, answer, queue)
        elif idx == 0:
            down_input(arr, idx, answer, queue)
        else:
            up_input(arr, idx, answer, queue)
            down_input(arr, idx, answer, queue)
    
print(bfs_solution())