def solution(N, number):
    dp = list()
    for i in range(1,9):
        # print(f"{i}개의 개수로 만들 수 있는 조합")
        n = len(dp)
        tmp = set()
        num = 0
        for _ in range(i):
            num = num * 10 + N
        tmp.add(num)
        
        for idx in range(n):
            # print(f"dp[{idx}] : {dp[idx]}, dp[{n - idx - 1}] : {dp[n - idx - 1]}")
            for x in dp[idx]:
                for y in dp[n - idx - 1]:
                    tmp.add(x + y)
                    tmp.add(x - y)
                    tmp.add(x * y)
                    if y != 0 and x%y == 0:
                        tmp.add(x / y)
                    
        if number in tmp:
            return i
        else:
            dp.append(tmp)
        # print(f"현재 만든 dp 조합 {dp}")
    return -1