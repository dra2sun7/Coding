mcnt = 0
idx = 0

for i in range(1, 1000000):
    cnt = 0
    x = i
    while x != 1:
        if x%2 == 0:
            x = x//2
            cnt += 1
        else:
            x = 3*x+1
            cnt += 1
    if mcnt < cnt:
        mcnt = cnt
        idx = i

print(idx)