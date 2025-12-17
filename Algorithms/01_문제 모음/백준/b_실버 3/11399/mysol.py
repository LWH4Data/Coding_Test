import sys, time
sys.stdin = open("input.txt")
start = time.time()

#============================================
# 입력값 받기
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

# 1부터 시작
for i in range(1, N):
    for j in range(1, i + 1):
        if numbers[i-j] > numbers[i]:
            if i - j == 0:
                temp = 

print(numbers)


# 앞과 뒤의 수를 비교

# 왼쪽 수보다 크지 않다면 더 자신보다 작거나 같은 수를 만날 때까지 이동

# 우측 수보다 작지 않다면 자신보다 크거나 같지 않은 수를 만날 때까지 이동.

print(N, numbers)
#============================================

end = time.time()
print("time:", start - end)