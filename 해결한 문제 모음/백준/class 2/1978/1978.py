import sys
sys.stdin = open('input_1978.txt')

N = int(input())
num = list(map(int, input().split()))
cnt = 0  # 소수 개수 카운트

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # √n 까지만 확인
        if n % i == 0:
            return False
    return True

# 입력된 숫자 중 소수 개수 확인
for x in num:
    if is_prime(x):
        cnt += 1

print(cnt)
