import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=================================================================
"""
브루트포스가 된다면 브루트포스를 먼저 적용하는 것이 좋다.
"""
# 연산 델타
d = (1, 3)

# 입력값 받기
nums = sys.stdin.readline().strip()
nums = list(nums)

# 연산 수행
total_sum = 0
check = 0

for i in range(len(nums)):
    
    # 별표인 경우는 skip
    if nums[i] == '*':
        # 몇 번째 수인지 기록
        check = i
        continue
    
    # 아닌 경우 연산
    else:
        total_sum += int(nums[i]) * d[i % 2]

# 정답 찾기
# 0 ~ 9까지 전체 대입(브루트포스)
for i in range(10):
    # *이 짝수번째 수인 경우
    if check % 2 == 0:
        temp_sum = total_sum + i
    # *이 홀수번째 수인 경우
    else:
        temp_sum = total_sum + 3 * i

    # 10으로 나뉘어 떨어지는 값을 찾는다면 정답
    if temp_sum % 10 == 0:
        print(i)
        break
#=================================================================

e_t = time.time()
print("time: ", e_t - s_t)