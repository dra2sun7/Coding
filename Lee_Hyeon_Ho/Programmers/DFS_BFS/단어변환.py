from collections import deque
def check_word(begin, words, queue, cnt):
    global n
    k = 0
    while len(words) != k:
        tmp = 0
        for i in range(n):
            if words[k][i] != begin[i]:
                tmp += 1
        if tmp == 1:
            queue.append((words.pop(k), cnt))
        else:
            k += 1

def solution1(begin, target, words):
    global n
    queue = deque()
    n = len(begin)    

    if target not in words:
        return 0
    
    check_word(begin, words, queue, 1)

    while queue:
        begin, cnt = queue.popleft()
        
        if begin == target:
            return cnt
        
        check_word(begin, words, queue, cnt+1)
    
    return 0

def check_word(begin, visited, words, queue, cnt):
    global n
    k = 0
    for x in words:
        if x not in visited:
            if sum([w1 != w2 for w1, w2 in zip(begin, x)]) == 1:
                queue.append((x, cnt))
                visited.add(x)
        
def solution2(begin, target, words):
    global n
    queue = deque([(begin, 0)])
    n = len(begin)    
    visited = set()

    if target not in words:
        return 0
    
    while queue:
        begin, cnt = queue.popleft()
        
        if begin == target:
            return cnt
        
        check_word(begin, visited, words, queue, cnt+1)
    
    return 0