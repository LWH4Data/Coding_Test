import sys, time
sys.stdin = open("input.txt")
start = time.time()

#================================================
# 입력값을 받는다.
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
# 전체 합 배열을 초기화한다.
#   ● append 방식은 추후 값 업데이트가 힘들다.
total_sum = [0] * (N + 1)
ans = 0

# 전체 합을 구현한한다.
for i in range(1, N + 1):
    total_sum[i] += total_sum[i-1] + numbers[i-1]
# print(total_sum)

# 이중 for loop을 통한 방법으로 수정.
#   ● 투 포인터를 활용
for k in range(0, len(total_sum) - 1):
    for j in range(k, len(total_sum)):
        # 구간 합 초기화
        temp = total_sum[j] - total_sum[k]
        # print(temp)

        # M으로 나누어 떨어지면 ans 증가.
        if temp % M == 0:
            ans += 1

print(ans - len(numbers))
#================================================

end = time.time()
print("time:", end - start)

# # 하단의 과정을 좌측 포인터를 N - 1번 이동하면서 반복
# for k in range(1, N):

#     # 다시 초기화 하지 않고 

#     # M으로 나누었을 때 떨어지는 경우를 count 한다.
#     for j in range(k, len(total_sum)):
#         if total_sum[j] % M == 0:
#             ans += 1