def is_prime(num):
    for x in range(2, num):
        if num//x < x:
            break
        
        if num%x == 0:
            return False
        
    return True

sum = 0
for i in range(2, 2000001):
    if is_prime(i):
        sum += i
    # print(f"지금 값 : {i}, 소수임? : {is_prime(i)}")

print(sum)