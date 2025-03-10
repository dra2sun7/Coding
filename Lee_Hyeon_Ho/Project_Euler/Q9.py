
def cal():
    for a in range(999):
        for b in range(a+1, 1000):
            for c in range(b+1, 1001):
                if (a*a + b*b) == (c*c) and (a + b + c) == 1000:
                    return a*b*c
                    
print(cal())