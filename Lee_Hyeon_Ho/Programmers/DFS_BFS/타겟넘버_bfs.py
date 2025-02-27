from collections import deque

def bfs(numbers, target):
    global cnt
    
    queue = deque([(0,0)])
    
    while queue:
        snum, idx = queue.popleft()
        
        if idx == len(numbers):
            print(queue)
            if snum == target:
                cnt += 1
            continue
            
        queue.append((snum+numbers[idx], idx+1))
        queue.append((snum-numbers[idx], idx+1))

    

def solution(numbers, target):
    global cnt
    cnt = 0
    bfs(numbers,target)
    return cnt