"""
< 시간 복잡도 >
"""
import sys, time
sys.stdin = open("input.txt")
start = time.time()

#===================================
# 입력값 받기
N, S = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))
ans = 0

# 합 배열 생성
sum_num = [0] * len(numbers)
sum_num[0] = numbers[0]

for i in range(1, len(numbers)):
    sum_num[i] = sum_num[i - 1] + numbers[i]

# 합 배열을 통해 구간 합 구하기
for _ in range(S):
    num_start, num_end = map(int, sys.stdin.readline().split())
    
    # num_start - 2가 음수라면 다음 처리.
    if num_start - 2 < 0:
        ans = sum_num[num_end - 1]
    else:
        ans = sum_num[num_end - 1] - sum_num[num_start - 2]
    print(ans)
#===================================

end = time.time()

print("time:", end-start)