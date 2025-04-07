N,K = map(int, input().split(" "))
dp = [[0  for _ in range(K+1)] for _ in range(N+1)]
arr = [[0, 0]]
for _ in range(N):
    x, y = map(int, input().split(" "))
    arr.append([x, y])

# 중복 불가 문제
# arr.sort(reverse=True)
# for i in range(N):
#     for w in range(K,arr[i][0]-1, -1):
#         dp[w] = max(dp[w], dp[w-arr[i][0]] + arr[i][1])
# print(max(dp))


# 중복 가능 문제
# arr.sort()

# for i in range(N):
#     for w in range(arr[i][0], K+1):
#         dp[w] = max(dp[w], dp[w-arr[i][0]] + arr[i][1])

# print(max(dp))

for i in range(1, N+1):
    weight, value = arr[i]
    
    for w in range(K+1):
        if w < weight:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)

answer = 0
for x in dp:
    k = max(x) 
    if k > answer:
        answer = k
        
print(answer)