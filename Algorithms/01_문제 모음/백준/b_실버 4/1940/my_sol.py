import sys, time
sys.stdin = open("input.txt")
start = time.time()

#======================================
# 입력 받기
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
ans = 0

# 이중 for loop을 통한 풀이.
for i in range(N-1):
    for j in range(i + 1, N):

        # 두 수의 합을 비교하여 답을 연산.
        if numbers[i] + numbers[j] == M:
            ans += 1

print(ans)
#======================================

end = time.time()
print("time:", end - start)