import sys

N, T = sys.stdin.readline().strip().split(" ")
dict = set()

N = int(N)

for _ in range(N):
    name = sys.stdin.readline().strip()
    
    if name not in dict:
        dict.add(name)
    
if T == "Y":
    print(len(dict))
elif T == "F":
    print(len(dict)//2)
else:
    print(len(dict)//3)
    