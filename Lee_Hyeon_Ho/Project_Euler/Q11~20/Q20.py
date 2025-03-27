arr = [1]

for x in range(2, 101):
    for i in range(len(arr)-1, -1, -1):
        num = arr[i] * x # 현재 자리에 곱한 값
        if num >= 10:
            if i == len(arr) - 1:
                arr.append(num//10)
                arr[i] = num%10
            else:
                arr[i+1] += (num//10)
                arr[i] = num%10
        else:
            arr[i] = num
    
    
    for i in range(len(arr)):
        if arr[i] >= 10:
            if i == len(arr) - 1:
                arr.append(arr[i]//10)
                
            else:
                arr[i+1] += (arr[i]//10)
            arr[i] = arr[i]%10
    
sum = 0
for x in arr:
    sum += x
print(sum)