import sys
sys.setrecursionlimit(10**6)

arr = []
answer = set()

for _ in range(5):
    tmp = list(sys.stdin.readline().strip().split(" "))
    arr.append(tmp)
    
def dfs(arr, x, y, st):
    global answer
    tmp = [(0,1),(1,0),(-1,0),(0,-1)]
    # print(f"st : {st}")
    # print("==================")
    for a, b in tmp:
        nx =  x+a; ny = y+b
        if (-1 < nx < 5 and -1 < ny < 5):
            st.append(arr[nx][ny])
            if len(st) == 6:
                answer.add("".join(st))
            else:
                dfs(arr, nx, ny, st)
            st.pop()

for i in range(5):
    for j in range(5):
        # print()
        dfs(arr, i, j, [arr[i][j]])

print(len(answer))