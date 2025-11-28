import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=====================================
T = int(input())

for _ in range(1, T + 1):
    # 입력값 받기
    N = int(input())
    numbers = input()
    ans = 0

    # 순회하며 합 구하기
    for i in range(N):
        ans += int(numbers[i])

    print(ans)
#=====================================

end = time.time()

print("time: ", end-start)