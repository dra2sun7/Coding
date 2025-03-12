n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[i][0] = 1
    arr[0][i] = 1
    
for y in range(1, n):
    for x in range(1, n):
        arr[x][y] = arr[x-1][y] + arr[x][y-1]



for x in arr:
    print(x)