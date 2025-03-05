answer = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        num = str(x * y)
        if num == num[::-1]:
            if answer < int(num):
                answer = int(num)
                
                
print(answer)