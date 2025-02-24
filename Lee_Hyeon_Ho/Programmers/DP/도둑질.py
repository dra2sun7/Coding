def solution(money):
    n = len(money)
    dp1 = [money[0], money[1]]
    dp2 = [money[1], money[2]]

    # Solution1 시간 문제 발생    
    
    # for i in range(2, n-1):
    #     dp1.append(max(money[i] + max(dp1[:i-1]), max(dp1[:i])))
    #     dp2.append(max(money[i+1] + max(dp2[:i-1]), max(dp2[:i])))
    
    # Solution2 
    # dp1[:] 해당 방식은 O(n)의 시간을 소요하기 때문에 복잡도가 늘어남
    pmax1 = money[0]
    pmax2 = money[1]
    
    for i in range(2, n-1):
        dp1.append(max(money[i] + pmax1, dp1[i-1]))
        pmax1 = max(pmax1, dp1[i-1])
        dp2.append(max(money[i+1] + pmax2, dp2[i-1]))
        pmax2 = max(pmax2, dp2[i-1])
        
    # print(f"첫번째 선택 dp1 : {dp1}, 마지막 선택 dp2 : {dp2}")

    return max(dp2[-1], dp1[-1])
