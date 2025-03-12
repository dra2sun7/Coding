snum = 0
num = 1

for i in range(1000):
    num *= 2


for x in str(num):
    snum += int(x)
print(snum)