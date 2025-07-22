import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#============================================
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 필요한 변수 초기화
    cnt = 0 # 주식의 수
    total_sum = 0 # 누적합
    idx = 0 # 현재 idx
    target = max(nums) # 현재 최대값
    Ans = 0 # 정답

    while idx < len(nums):

        # 시작값이 최대면 아무것도 하지 않고 넘어감
        if nums[idx] == target:
            continue

        # 현재 값이 최대값이 아니면 누적합을 하고 cnt += 1
        if nums[idx] != target:
            total_sum += nums[idx]
            cnt += 1

        # 최대값일 경우 수익 실현
        else:
            Ans += nums[idx] - total_sum

            # 만약 마지막 원소면 출력 후 종료
            if idx == len(nums) - 1:
                print(Ans)
                break

            # 나머지 변수 다시 초기화
            cnt = 0
            total_sum = 0
            target = max(nums[idx + 1 : ])
        
        # idx 추가
        idx += 1
#============================================

end_time = time.time()
print('time :', end_time - start_time )

'''
< 로직 >
1. 무조건 최대값일 때 팔고, 다시 구매하면서 진행해야 한다.
'''

'''
< 시간 복잡도 >
- 최대값을 찾는데 O(N)

- 전체를 한 번 순환하기에 O(N)

- 따라서 O(2N) = O(N)
'''

'''
< 문제 정리 >
1. 하나 사기, 원하는 만큼 팔기, 아무 행도 안하기.

2. 최대 이익을 나타내는 정수 출력.

3. 날의 수(N)의 최대값이 1,000,000이기에 절대 완탐은 불가.
'''