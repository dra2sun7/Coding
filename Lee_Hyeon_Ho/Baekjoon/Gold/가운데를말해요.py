import heapq
import sys

min_heap = []
max_heap = []
# arr = []
N = int(sys.stdin.readline())
heapq.heappush(max_heap, int(input()) * -1)
print(-max_heap[0])
# arr.append(-max_heap[0])

for i in range(1, N):
    
    x = int(sys.stdin.readline())
    # print(f"현재 담긴 개수 : {i}")
    # print(f"작업 전 상태")
    # print(f"max_heap : {max_heap}")
    # print(f"min_heap : {min_heap}")
    # 현재 담긴 개수가 홀수인 경우
    if i%2 != 0:
        if -max_heap[0] <= x:
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(max_heap, -x)
            heapq.heappush(min_heap, heapq.heappop(max_heap) * -1)
            
    # 현재 담긴 개수가 짝수인 경우
    else:
        if -max_heap[0] <= x:
            heapq.heappush(min_heap, x)
            heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)
        else:
            heapq.heappush(max_heap, -x)
    # print(f"max_heap : {max_heap}")
    # print(f"min_heap : {min_heap}")
    print(-max_heap[0])
    # arr.append(-max_heap[0])
# print(arr)