import time
import sys

# # make_input.py
# with open("input.txt", "w") as f:
#     for _ in range(30**5):  # 10만 줄 입력 생성
#         f.write("123\n")

# input() 테스트
with open("input.txt", "r") as f:
    sys.stdin = f  # 표준 입력을 input.txt로 바꿔줌

    start = time.time()
    for _ in range(30**5):
        a = input()
    end = time.time()
    print("input() 방식:", end - start)

# sys.stdin.readline() 테스트
with open("input.txt", "r") as f:
    sys.stdin = f  # 다시 초기화

    start = time.time()
    for _ in range(30**5):
        a = sys.stdin.readline()
    end = time.time()
    print("readline() 방식:", end - start)

a = sys.stdin.readline()

print("마지막 문자 =============")
print(a[-1], end="")
print("마지막 문자 =============")