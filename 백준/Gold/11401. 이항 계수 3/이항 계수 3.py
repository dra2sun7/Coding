import sys

MOD = 1000000007



# 3. 이항계수 함수
def nCk(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
MAX, k = map(int, sys.stdin.readline().split(" "))

fact = [1] * (MAX + 1)
inv_fact = [1] * (MAX + 1)

# 1. 팩토리얼 계산
for i in range(1, MAX + 1):
    fact[i] = fact[i-1] * i % MOD

# 2. 역팩토리얼 계산 (페르마의 소정리 이용)
inv_fact[MAX] = pow(fact[MAX], MOD - 2, MOD)
for i in range(MAX, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD

print(nCk(MAX, k))