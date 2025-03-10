def dfs(tickets, spot, arr, visited):
    global answer
    if len(visited) == len(tickets):
        if answer == None or answer > arr:
            # print("===========================")
            # print(f"바꾸기 전 : {answer}")
            answer = arr[:]
            # print(f"바꾼 후 : {answer}")
            # print("===========================")
        return
    
    for i in range(len(tickets)):
        if i not in visited and tickets[i][0] == spot:
            arr.append(tickets[i][1])
            visited.add(i)
            # print(f"현재 위치 : {tickets[i][0]}, 다음 위치 : {tickets[i][1]}")
            # print(f"visited : {visited}, arr : {arr}")
            dfs(tickets, tickets[i][1], arr, visited)
            arr.pop()
            visited.remove(i)

def solution(tickets):
    global answer
    answer = None
    dfs(tickets, "ICN", ["ICN"], set())
    return answer