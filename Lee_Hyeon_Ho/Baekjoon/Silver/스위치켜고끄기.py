import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())

for _ in range(M):
    s, num = map(int, sys.stdin.readline().split(" "))
    
    if s == 1:
        for i in range(num-1, N, num):
            arr[i] = 1 - arr[i]
            
    else:
        cnt = 1
        num -= 1
        arr[num] = 1 - arr[num]
        while num + cnt < N and num - cnt > -1:
            if arr[num+cnt] != arr[num-cnt]:
                break
            arr[num+cnt] = 1 - arr[num+cnt]
            arr[num-cnt] = 1 - arr[num-cnt]
            cnt += 1
    # print("===========결과===========")
    # print(" ".join(list(map(str, arr))))
    # print("===========결과===========")
      
idx = 0
while idx < N:
    if (idx+1)%20 == 0:
        print(arr[idx])
    else:
        print(arr[idx],end=" ")
    idx += 1
