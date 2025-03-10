def check_prime(num):
    for x in range(2, num):
        if num//x < x:
            break
        
        if num%x == 0:
            return False
    
    return True
    
num = 600851475143
answer = 0
for x in range(2, num):
    if num//x < x:
        break

    if num%x == 0:
        y = num//x
        if check_prime(x):
            if answer < x:
                answer = x
        if check_prime(y):
            if answer < y:
                answer = y

print(answer)