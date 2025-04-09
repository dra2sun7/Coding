# 한개 또는 세개...
# 1 SK
# 2 CY
# 3 SK
# 4 CY
# 5 SK
# 6 CY
# 7 ...?
# 애초에 홀짝이기 때문에 홀수 개수가 홀수때 이기고 짝수 개수가 짝수때 이기는거 아님?

import sys

N = int(sys.stdin.readline())

if N%2 == 0:
    print("CY")
else:
    print("SK")
    