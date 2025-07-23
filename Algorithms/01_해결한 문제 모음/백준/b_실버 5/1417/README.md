# 1. 정리
## 1-1. 로직
- 가장 큰 수를 찾고 첫 번째 원소와 비교하면 된다. 
- 가장 큰 수와의 비교만 탐욕적으로 반복

## 1-2. 시간 복잡도 
- 솔루션의 시간 복잡도는 $O(nlogn)$
    - heappush와 heappop의 시간 복잡도가 O(logn)이고, 이를 각 후보 n 명마다 반복하기 때문.

## 1-3. 메모
1. 그리디 문제를 정렬할 때 sort()나 sorted()를 활용하는 것이 아니라 `heapq`를 활용할 수도 있음.

# 2. 내 풀이
- 완탐 + 시뮬 형식으로 시도할라 했으니 시간이 너무 오래 걸리는 방법임.
```python 
import sys, time
sys.stdin = open('input_1417.txt')
start_time = time.time()

#======================================================
def sol():
    cnt = 0
    
    while True:
        
        # 유일 최대값이면 반환
        if nums.index(max(nums)) == 0 and cnt == 0:

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
```

# 3. 솔루션
```python
import sys, time
sys.stdin = open('input_1417.txt')
start_time = time.time()

#======================================================
import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dasom = int(input())
    others = []

    # 후보가 한 명인 경우 0을 출력.
    if N == 1:
        print(0)

        # 0출력 후 이후 코드는 실행되면 안 되기 때문에 skip
        continue

    for _ in range(N - 1):
        # heapq를 자료구조를 사용.
        # others에 각 후보의 지지자들을 push하는데 음수로 두어 최대힙 처럼 작동하도록 함.
        heapq.heappush(others, -int(input()))

    cnt = 0

    while others:
        # 최대 지지자 수를 반환
        max_vote = -heapq.heappop(others)

        # 다솜이가 최대지지자인 경우 종료
        if dasom > max_vote:
            break

        # 아닌 경우 한 명씩 매수하고, cnt 기록
        dasom += 1
        max_vote -= 1
        count += 1

        heapq.heappush(others, -max_vote)

    # 정답 출력.
    print(count)
#======================================================

end_time = time.time()
print('time :', end_time - start_time)
```