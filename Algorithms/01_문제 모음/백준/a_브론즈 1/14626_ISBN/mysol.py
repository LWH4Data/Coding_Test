import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=================================================================
# 연산 덽타
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
        check = i
        continue
    
    # 아닌 경우 연산
    else:
        total_sum += int(nums[i]) * int(d[i % 2])

ans = 10 - total_sum % 10

if check // 2 == 0:
    print(ans)
else:
    print(int(ans / 3))
#=================================================================

e_t = time.time()
print("time: ", e_t - s_t)