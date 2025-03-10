def check_prime(num):
    for x in range(2, num):
        if num//x < x:
            break
        
        if num%x == 0:
            return False
        
    return True

cnt = 0
num = 2

while cnt < 10001:
    if check_prime(num):
        cnt += 1
    num += 1
    
print(num-1)