def count_div(num):
    cnt = 0
    for x in range(1, num):
        if num//x < x:
            break
        if num%x == 0:
            if num//x == x:
                cnt += 1
            else:
                cnt += 2
    return cnt

num = 1
sum = 0

while True:
    sum += num
    if count_div(sum) < 500:
        num += 1
        continue
    
    else:
        print(sum)
        break