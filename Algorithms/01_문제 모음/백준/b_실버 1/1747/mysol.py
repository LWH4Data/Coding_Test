import sys, time
sys.stdin = open("input.txt")
start = time.time()

#===================================================
import math

# 입력값 받기
N = int(sys.stdin.readline())

# 에라토스테네스의 체 구현
nums = [0] * 10**7
for i in range(0, len(nums)):
    nums[i] = i

for i in range(2, int(math.sqrt(10**7))):
    for j in range(i + i, len(nums), i):
        nums[j] = 0

print(nums)

# flag = False

# for num in nums:

#     if num == 0:
#         continue

    # 펠린드롬인지 확인.
    # 짝수
    # if num >= N:
    #     if len(str(num)) % 2 == 0:
    #         for j in range(0, int(len(str(num)) / 2)):
    #             if str(num)[j] != str(num)[-1 - j]:
    #                 break
    #             flag = True
    #             print(num)
    #             break
        
    #     if len(str(num)) % 2 == 1:
    #         for j in range(0, int(len(str(num)) / 2)):
    #             if str(num)[j] != str(num)[-1 - j]:
    #                 break
    #             flag = True
    #             print(num)
    #             break



# N보다 크면서 가장 작은 소수를 찾는다.

# 찾은 소수가 펠린드롬인지 확인한다.
#===================================================

end = time.time()
print("time: ", end - start)

# 1,000,000 ~ 10,000,000 사이의 적어도 한 수는 펠린드롬이다. 라는 가설.
# 위가 충족 되어야 10**6 ~ 10**7 사이의 소수를 찾아 문제 해결.
# 10**7을 초과하는 경우 공간 복잡도가 터진다.