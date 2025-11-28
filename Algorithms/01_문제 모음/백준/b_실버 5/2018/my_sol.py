import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=======================================
# 입력값 받기
N = int(sys.stdin.readline())
ans = 0

# 1부터 하나씩 더하기 시작
for i in range(1, N // 2 + 1):
    # 첫 번째 포인터 초기화
    temp = i

    # 두 번째 포인터 시작.
    for j in range(i + 1, N // 2 + 2):
        # 두 번째 포인터를 움직이며 합을 구현.
        temp += j

        # N과 같다면 중단.
        if temp == N:
            ans += 1
            break
        
        # N을 초과해도 중단.
        if temp > N:
            break

print(ans + 1)
#=======================================

end = time.time()
print("time:", end - start)