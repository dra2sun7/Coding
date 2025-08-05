import sys
arr = []

for _ in range(3):
    arr.append(sys.stdin.readline().strip())

print(int(arr[0]) + int(arr[1]) - int(arr[2]))
print(int(str(arr[0]) + str(arr[1])) - int(arr[2]))