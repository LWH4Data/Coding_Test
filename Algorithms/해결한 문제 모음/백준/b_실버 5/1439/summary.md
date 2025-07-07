# 1. 정리
## 1-1. 풀이
- 0의 덩이와 1의 덩이 중 더 작은 덩이가 항상 최적해가 된다.
## 1-2. 시간 복잡도
- 전체를 1회 순회하기에 `O(N)`이 된다.
## 1-3. 주의(최적화)
- 나의 경우 while문 내부에서 모든 작업을 처리하는데 첫 문자 부분을 따로 처리하고 순회하면 시간 복잡도를 줄일 수 있다.
```python
z_cnt = 0
o_cnt = 0

if nums[0] == '0':
    z_cnt += 1
else:
    o_cnt += 1

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        if nums[i] == '0':
            z_cnt += 1
        else:
            o_cnt += 1
```

# 2. 내 풀이.
```python
import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#=======================================
T = int(input())

for tc in range(1, T + 1):
    nums = input()

    i = 0
    # 0의 덩어리 수
    z_cnt = 0
    # 1의 덩어리 수
    o_cnt = 0
    while i < len(nums):

        # 첫 번째 글자가 0이면 0덩어리에 추가.
        if i == 0 and nums[i] == '0':
            z_cnt += 1

        # 첫 번째 글자가 1이면 1덩얼리에 추가.
        if i == 0 and nums[i] == '1':
            o_cnt += 1
        
        # 순회하면서 이전 원소와 다른 경우 각 덩어리에 추가.
        if i != 0 and nums[i - 1] != nums[i]:
            if nums[i] == '0':
                z_cnt += 1
            if nums[i] == '1':
                o_cnt += 1
        
        i += 1

    # 최소인 값을 출력.
    print(min(z_cnt, o_cnt))
#=======================================

end_time = time.time()
print('time: ', end_time - start_time)

'''
< 로직 >
1. 0과 1의 덩어리 중 더 작은 덩어리의 수를 출력하면 된다.
    -> 더 작은 덩어리가 항상 최적해이기 때문.
    -> 뒤집어 출력하는 문제는 아니기에 뒤집을 필요는 없다.
'''

'''
< 시간 복잡도 >
- 전체 1회 순회하면서 변환하기에 O(N)이다.
'''

'''
< 문제 정리 >
'''
```