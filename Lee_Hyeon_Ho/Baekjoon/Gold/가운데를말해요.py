import heapq

max_heap = []
min_heap = []
N = int(input())

for i in range(N):
    # heapq.heappush(max_heap, int(input()) * -1)
    
    # if min_heap and max_heap[0] * -1 > min_heap[0]:
    #     heapq.heappush(min_heap, heapq.heappop(max_heap) * -1)
        
    # ##########################################################################################
    
    # if len(max_heap) > len(min_heap) + 1:
    #     heapq.heappush(min_heap, heapq.heappop(max_heap) * -1)
    # elif len(max_heap) < len(min_heap):
    #     heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)
    # # print(f"max_heap : {max_heap}")
    # # print(f"min_heap : {min_heap}")
    # print(max_heap[0] * -1)
    x = int(input())
    
    if max_heap == []:
        heapq.heappush(max_heap, x * -1)
        
    else:
        # 현재 담긴 숫자가 홀수개인 경우
        if i%2 != 0:
            if max_heap[0] * -1 <= x:
                heapq.heappush(max_heap, x * -1)
                heapq.heappush(min_heap, heapq.heappop(max_heap) * -1)
            else:
                heapq.heappush(min_heap, x)
        else:
            if max_heap[0] * -1 <= x:
                heapq.heappush(max_heap, x * -1)
            else:
                heapq.heappush(min_heap, x)
                heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)
    # print(f"max_heap : {max_heap}")
    # print(f"min_heap : {min_heap}")
    print(max_heap[0] * -1)
    