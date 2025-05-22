T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, list(input().strip().split(" "))))
    dp = set([0])
    
    for x in arr:
        tmp = set()
        for y in dp:
            num = x+y
            tmp.add(num)
        dp.update(tmp)
    print(f"#{i+1} {len(dp)}")
    