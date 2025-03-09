from collections import deque
def draw_box(rectangle):
    arr = [[0 for _ in range(102)] for _ in range(102)]
    for k in rectangle:
        x1, y1, x2, y2 = k
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                arr[x][y] = 1
    
    for k in rectangle:
        x1, y1, x2, y2 = k
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        
        # 내부는 0으로 처리
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                arr[x][y] = 0
    
    return arr

def solution(rectangle, characterX, characterY, itemX, itemY):
    arr = draw_box(rectangle)
    visited = [[False for _ in range(102)] for _ in range(102)]
    queue = deque([(characterX * 2, characterY * 2, 0)])
    visited[characterX * 2][characterY * 2] = True

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y, cnt = queue.popleft()
        if (x, y) == (itemX * 2, itemY * 2):
            return cnt // 2
        
        for a, b in move:
            if (0 <= x+a < 102 and 0 <= y+b < 102) and not visited[x+a][y+b] and arr[x+a][y+b] == 1:
                visited[x+a][y+b] = True
                queue.append((x+a, y+b, cnt+1))

    return 0



# 틀린 방법, 해당 방식은 내부로 삽입되는 경로 또한 포함된다.

# from collections import deque
# def find_location(queue, diagram, x, y, cnt):
#     if x == diagram[0]:
#         if y >= diagram[1] and y <= diagram[3]:
#             queue.append((x, y, cnt+1))
            
#     elif x == diagram[2]:
#         if y >= diagram[1] and y <= diagram[3]:
#             queue.append((x, y, cnt+1))
            
#     elif y == diagram[1]:
#         if x >= diagram[0] and x <= diagram[2]:
#             queue.append((x, y, cnt+1))
            
#     elif y == diagram[3]:
#         if x >= diagram[0] and x <= diagram[2]:
#             queue.append((x, y, cnt+1))

# def solution(rectangle, characterX, characterY, itemX, itemY):
#     queue = deque([(characterX, characterY, 0)])
    
#     while queue:
#         x, y, cnt = queue.popleft()

#         if (x, y) == (itemX, itemY):
#             return cnt

#         for diagram in rectangle:
#             find_location(queue, diagram, x+1, y, cnt)
#             find_location(queue, diagram, x-1, y, cnt)
#             find_location(queue, diagram, x, y-1, cnt)
#             find_location(queue, diagram, x, y+1, cnt)
    
#     print(queue)
    
#     return 0