import sys

def solution():
    P = int(sys.stdin.readline())
    
    for _ in range(P):
        T, *arr = list(map(int, sys.stdin.readline().strip().split(" ")))
        N = len(arr)
        solve = [arr[0]]
        cnt = 0
        
        for i in range(1, N):
            index = 0
            while index < i:
                if solve[index] > arr[i]:
                    solve.insert(index, arr[i])
                    cnt += i-index
                    break
                index += 1
            if index == i:
                solve.append(arr[i])
        print(T, cnt)

def Linked_List():
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            
    class LinkedList:
        def __init__(self):
            self.head = None
            
        def insert(self, index, data):
            new_node = Node(data)
            if index == 0:
                new_node.next = self.head
                self.head = new_node
                return
            
            cur = self.head
            for _ in range(index - 1):
                if not cur:
                    raise IndexError("Index out of range")
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
            
        def print_list(self):
            cur = self.head
            while cur:
                print(cur.value, end="->", flush="True")
                cur = cur.next
            print()
            

    P = int(sys.stdin.readline())

    for _ in range(P):
        T, *arr = sys.stdin.readline().strip().split(" ")
        
        head = LinkedList()
        head.insert(0, arr[0])
        min_index = 0
        min_tall = arr[0]
        cnt = 0
        
        for i in range(1, len(arr)):
            if arr[i] < min_tall:
                head.insert(min_index, arr[i])
                min_tall = arr[i]
                cnt += i-min_index
            else:
                head.insert(i, arr[i])
                
        # head.print_list()
        print(T, cnt)
        
solution()