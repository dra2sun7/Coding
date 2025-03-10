sum = 0

for x in range(1, 101):
    for y in range(1, 101):
        if x == y:
            continue
    
        sum += x * y
        
print(sum)