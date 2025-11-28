"""
< 시간 복잡도 > 
- O(N)
"""
import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=====================================
T = int(sys.stdin.readline())

for _ in range(T):
    # 변수 초기화
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))

    # 최고 점수 M을 찾는다.
    max_val = max(numbers)
    # print(max_val)

    # 점수 / M * 100을 통해 모든 값을 변환한다.
    for i in range(len(numbers)):
        numbers[i] = numbers[i] / max_val * 100
    # print(numbers)

    # 평균을 구한다.
    ans = sum(numbers) / len(numbers)
    print(ans)
#=====================================

end = time.time()
print("time:", end-start)