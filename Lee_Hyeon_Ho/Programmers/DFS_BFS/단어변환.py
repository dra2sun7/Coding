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

def solution(begin, target, words):
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