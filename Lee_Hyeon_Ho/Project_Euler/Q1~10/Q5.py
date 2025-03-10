def check_prime(num):
    for x in range(2, num):
        if (num//x) < x:
            break
    
        if num%x == 0:
            return False
        
    return True

def find_multi(x, num):
    for k in range(x,0,-1):
        if x%k == 0 and num%k == 0:
            return x//k
            
                
    return 1
    
answer = 1

for x in range(2, 20):
    if check_prime(x):
        print(f"해당 숫자 {x}가 소수이기 때문에 곱한다.")
        answer *= x
        
    else:
        answer = answer * find_multi(x, answer)
    print(answer)

print(answer)