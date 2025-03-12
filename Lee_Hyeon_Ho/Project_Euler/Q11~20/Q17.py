# one two three four five six seven eight nine ten
# eleven twelve thirteen fourteen fifteen sixteen eighteen nineteen
# twenty thirty, forty, fifty sixty seventy eighty ninety
# one hundred two hundred
sn = 0
arr1 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
# 0~19까지 정리

arr2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
# 20 30 ... 90

# 1~19까지 더한 값
for x in arr1:
    # print(x, end=" ")
    sn += len(x)
# print()

for x in arr2:
    for y in arr1:
        if y == "ten":
            break
        # print(f"{x} {y}", end=" ")
        sn += len(x) + len(y)

# 101~199, 201~299, ... 901~999에서 뒤 두자리를 전부 계산
sn = sn*10


for x in arr1:
    if x == "":
        continue
    if x == "ten":
        break
    
    sn += (len(x) + len("hundred and") - 1) * 99

for x in arr1:
    if x == "":
        continue
    if x == "ten":
        break
    
    sn += len(x) + len("hundred")

print(sn + len("ten thousand") - 1)
#     print(f"{x} hundred", end=" ")
# print()

