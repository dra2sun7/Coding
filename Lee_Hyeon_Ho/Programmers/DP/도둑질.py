
# Solution1 시간 문제 발생
def solution(money):
    n = len(money)
    dp1 = [money[0], money[1]]
    dp2 = [money[1], money[2]]
    
    for i in range(2, n-1):
        dp1.append(max(money[i] + max(dp1[:i-1]), max(dp1[:i])))
        dp2.append(max(money[i+1] + max(dp2[:i-1]), max(dp2[:i])))
        
    return max(dp2[-1], dp1[-1])