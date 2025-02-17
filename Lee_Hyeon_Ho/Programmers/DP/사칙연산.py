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
    

        
def solution(arr):
    global mn
    mn = None
    
    dfs(arr, len(arr))
    
    return mn

