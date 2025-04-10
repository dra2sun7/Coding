import sys

N = int(sys.stdin.readline())
arr = []
x, y = 0, 0
waist = 0
left_arm = 0
right_arm = 0
left_leg = 0
right_leg = 0

for _ in range(N):
    arr.append(list(sys.stdin.readline().strip()))

for i in range(N):
    tmp = 0
    for j in range(N):
        if arr[i][j] == "*":
            # print("여기가 머리임")
            x = i+1
            y = j
            tmp = 1
            break
    if tmp == 1:
        break

t = 1
# 오른팔
while y+t < N and arr[x][y+t] == "*":
    right_arm += 1
    t += 1
t = -1
# 왼팔
while y+t > -1 and arr[x][y+t] == "*":
    left_arm += 1
    t -= 1

t = 1
# 허리
while arr[x+t][y] == "*":
    waist += 1
    t += 1
    
# 왼다리 오른다리 같이
while (x+t < N):
    if arr[x+t][y-1] != "*" and arr[x+t][y+1] != "*":
        break
    
    if arr[x+t][y-1] == "*":
        left_leg += 1
    
    if arr[x+t][y+1] == "*":
        right_leg += 1
    
    t += 1
    
print(x+1, y+1)
print(left_arm, right_arm, waist, left_leg, right_leg)
