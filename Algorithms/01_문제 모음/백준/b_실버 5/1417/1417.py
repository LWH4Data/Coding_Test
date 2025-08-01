import sys, time
sys.stdin = open('input_1417.txt')
start_time = time.time()

#======================================================
def sol():
    cnt = 0
    
    while True:
        
        # 유일 최대값이면 반환
        if nums.index(max(num)) == 0 and cnt == 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = []

    # 순회하면서 append
    for _ in range(N):
        nums.append(int(input()))

    # 만약 유일 후보면 0을 출력
    if len(nums) == 1:
        print(0)
        continue

    # 투 포인터
    a = nums[0]
    b = nums.index(max(nums))

    # 유일하게 첫 번째 원소가 최대일 때 종료

    while nums.index(max(nums)) != 0 and cnt != 0:


#======================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
- 첫 번째 원소와 가장 큰 원소를 비교

- 가장 큰 원소 -1, 첫 번째 원소 +1을 진행

- 첫 번째 원소의 크기가 최대값이 되면 종료.
'''

'''
< 시간 복잡도 >
- 사람이 중요한 것이 아니라 득표수가 중요.

- 따라서 최대 O(M), 득표 수 M의 최대는 100 이기에 O(100)
'''

'''
< 문제 정의 >
- 사람들이 누구를 투표할 지 알 수 있다.

- 후보 N 명, 주민 M 명

- 다솜이는 1 번, 다솜이가 아닌 사람을 투표하는 사람들을 매수하려 함.
    -> 모든 사람들의 득표수 보다 많은 득표 수를 갖도록
'''