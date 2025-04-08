import sys

H, W, N, M = map(int, sys.stdin.readline().split(" "))

width = (H+N)//(N+1)
height = (W+M)//(M+1)

print(width*height)

# 직접 모든 자리에 앉히기
# arr = [[0 for _ in range(W)] for _ in range(H)]
# move = [(1,0), (0,1), (1,1), (-1,0), (0,-1), (-1,-1), (1,-1), (-1,1)]
# cnt = 0

# for i in range(H):
#     for j in range(W):
#         if arr[i][j] != 0:
#             continue
        
#         arr[i][j] = 1
#         cnt += 1
        
#         for x,y in move:
#             if -1 < i+x < H and -1 < j+y < W and arr[i+x][j+y] == 0:
#                 arr[i+x][j+y] = 1
