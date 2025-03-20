def solution(n, times):
    right = n * max(times)
    left = min(times)
    mid = 0
    while left < right:
        mid = (left+right)//2
        cnt = 0
        for x in times:
            cnt += mid//x
        if cnt == n:
            break
        elif cnt > n:
            right = mid - 1
        else:
            left = mid + 1
    
    m = max(times)
    for x in times:
        if m > mid%x:
            m = mid%x
            
    return mid-m