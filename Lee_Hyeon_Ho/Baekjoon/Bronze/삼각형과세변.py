import sys

arr = list(map(int, sys.stdin.readline().split(" ")))
arr.sort()

while not (arr[0] == 0 and arr[1] == 0 and arr[2] == 0):
    if (arr[2] >= arr[0] + arr[1]) or (0 in arr):
        print("Invalid")
        
    else:
        if arr[0] == arr[1]:
            if arr[0] == arr[2]:
                print("Equilateral")
            else:
                print("Isosceles")
        else:
            if arr[1] == arr[2]:
                print("Isosceles")
            else:
                print("Scalene")
    
    arr = list(map(int, sys.stdin.readline().split(" ")))
    arr.sort()
    