def dfs(numbers, target, snum, idx):
    global cnt
    
    if idx == len(numbers):
        if snum == target:
            cnt += 1
        return

    dfs(numbers, target, snum+numbers[idx], idx+1)
    dfs(numbers, target, snum-numbers[idx], idx+1)
        
def solution(numbers, target):
    global cnt
    cnt = 0
    
    dfs(numbers, target, 0, 0)
    return cnt