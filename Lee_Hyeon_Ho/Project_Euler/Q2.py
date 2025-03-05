sum = 0
x = 1
y = 1
while x <= 4000000:
    tmp = x + y
    print(f"{x} + {y} = {tmp}")
    print(f"x = {x}, y = {y}, 합 = {tmp}")
    y = x
    x = tmp
    if tmp%2 == 0:
        sum += tmp
    
print(sum)