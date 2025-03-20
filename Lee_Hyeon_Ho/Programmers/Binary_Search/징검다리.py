def solution(distance, rocks, n):
    left = 1
    right = distance
    
    rocks.sort()
    rocks.append(distance)
    
    while left < right:
        mid = (left + right) // 2
        prev = 0
        remove = 0
        mn = distance
        i = 0
        
        while i < len(rocks):
            gap = rocks[i] - prev
            if gap < mid:
                remove += 1
            else:
                if mn > gap:
                    mn = gap
                    
                prev = rocks[i]
            i += 1
        if remove == n:
            return mn
        elif remove > n:
            right = mid - 1
        else:
            left = mid + 1
        
    return 0