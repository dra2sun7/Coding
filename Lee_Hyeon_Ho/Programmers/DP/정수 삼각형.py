def solution(triangle):    
    n = len(triangle)
    arr = [[-1 for i in range(j + 1)] for j in range(n)]
    
    arr[0][0] = triangle[0][0]
    print(arr)
    for x in range(n-1):
        for y in range(len(arr[x])):
            num = arr[x][y] + triangle[x+1][y]
            if num > arr[x+1][y]:
                arr[x+1][y] = num
            num = arr[x][y] + triangle[x+1][y+1]
            if num > arr[x+1][y+1]:
                arr[x+1][y+1] = num
        
    return max(arr[n-1])