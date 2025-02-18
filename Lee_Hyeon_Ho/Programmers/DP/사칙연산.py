# 1번 해결안 DFS
# 해당 방식은 복잡도가 너무 높음
def dfs(arr, n):
    global mn
    if n == 1:
        if mn == None:
            mn = int(arr[0])
        elif int(arr[0]) > mn:
            mn = int(arr[0])
        return 0
        
    for i in range(0, n-2, 2):
        num = ""
        if arr[i+1] == '+':
            num = str(int(arr[i]) + int(arr[i+2]))
        else:
            num = str(int(arr[i]) - int(arr[i+2]))
        # print(f"idx : {arr[i:i+3]}계산 된 값 : {num}, 다음으로 들어갈 배열 : {arr[:i] + [num] + arr[i+3:]}")        
        dfs(arr[:i] + [num] + arr[i+3:], n-2)
    
    
# 2번 해결안 DP
# 이거는 GPT가 알려줌... 너무 어렵네
def solution(arr):
    numbers = [int(arr[i]) for i in range(0, len(arr), 2)]
    operators = [arr[i] for i in range(1, len(arr), 2)]
    print(operators)
    n = len(numbers)
    dp_max = [[0 for _ in range(n)] for _ in range(n)]
    dp_min = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp_max[i][i] = numbers[i]
        dp_min[i][i] = numbers[i] 
    
    for size in range(2, n+1):
        for i in range(n - size + 1):
            j = i + size - 1
            dp_max[i][j] = float("-inf")
            dp_min[i][j] = float("inf")
            
            for k in range(i,j):
                if operators[k] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])
    
    return dp_max[0][n-1]


        
def solution(arr):
    numbers = [int(arr[i]) for i in range(0, len(arr), 2)]
    operators = [arr[i] for i in range(1, len(arr), 2)]
    print(operators)
    n = len(numbers)
    dp_max = [[0 for _ in range(n)] for _ in range(n)]
    dp_min = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp_max[i][i] = numbers[i]
        dp_min[i][i] = numbers[i] 
    
    for size in range(2, n+1):
        for i in range(n - size + 1):
            j = i + size - 1
            dp_max[i][j] = float("-inf")
            dp_min[i][j] = float("inf")
            
            for k in range(i,j):
                if operators[k] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])
    
    return dp_max[0][n-1]

