import bisect

def search(arr, target):
    cnt = 0
    idx = 0
    while idx < len(arr):
        cnt += 1
        if arr[idx] == target:
            return cnt
        idx += 1
    return -1
    
def binary_search(arr, target):
    cnt = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return cnt + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        cnt += 1

    return -1  # 존재하지 않는 경우 -1 리턴


arr = [i for i in range(1, 101)]
target = 35

print(binary_search(arr, target))
print(search(arr, target))

idx = bisect.bisect_left(arr, target)
right = bisect.bisect_right(arr, target)

print(idx, right)

# bisect.insort_left(arr, 35)

# print(arr)

bisect.insort_right(arr, 35)

print(arr)