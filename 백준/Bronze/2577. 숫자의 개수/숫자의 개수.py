import sys

num = 1
arr = [0] * 10

for _ in range(3):
    num *= int(sys.stdin.readline())

num = str(num)

for x in num:
    arr[int(x)] += 1
    
for x in arr:
    print(x)