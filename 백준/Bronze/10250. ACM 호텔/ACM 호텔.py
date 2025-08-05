import sys

T = int(sys.stdin.readline())
li = []

for _ in range(T):
    answer = ""
    H, W, N = map(int, sys.stdin.readline().split(" "))
        
    num1 = N%H      # 앞자리
    num2 = N//H     # 뒷자리
    
    if num1 == 0:
        num1 = H
        num2 -= 1
    
    num1 = str(num1); num2 = str(num2 + 1)
    for i in range(len(num1)):
        answer += num1[i]
    if len(num2) == 1:
        answer += "0"
    for i in range(len(num2)):
        answer += num2[i]
    
    li.append(answer)
    # print("".join(answer))

for x in li:
    print(x)
    