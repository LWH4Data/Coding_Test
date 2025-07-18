# 1. 정리
## 1-1. 풀이
- 처음에는 최소값을 찾고 해당 위치를 기준으로 합을 만들어 가는 것이었음.
- 그런데 이러면 최대값 보장이 안됨.
- 따라서 그리디 형식으로 최대값을 찾고 최대값을 기준으로 병합을 진행해야 함.

## 1-2. 시간 복잡도
- max()와 pop()의 과정에서 각자 O(N)이 걸리기에 전체 시간 복잡도는 $O(N^2)$이 된다.

## 1-3. 메모
- remove: 값을 기반으로 리스트 원소를 제거한다.
- pop: index를 기준으로 리스트 원소를 제거한다.

<br><br>

# 2. 내 풀이
```python
import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#=================================================
N = int(input())
num = list(map(int, input().split()))

# 변수 선언
temp_min = 0
Ans = 0

# while문을 통해 len(num) == 1일 때까지 반복
while len(num) != 1:

    # 최대값 연산을 위한 인덱스 저장.
    max_idx = num.index(max(num))

    # 최소값의 양 옆 값을 비교
    # 예외 처리
    # min_idx가 0인 경우
    if max_idx == 0:
        Ans += num[max_idx + 1] + num[max_idx]
        num.pop(max_idx + 1)
        continue

    # min_idx가 끝 idx인 경우
    if max_idx == len(num) - 1:
        Ans += num[max_idx - 1] + num[max_idx]
        num.pop(max_idx - 1)
        continue

    # 나머지는 양쪽 비교 후 합
    if num[max_idx - 1] > num[max_idx + 1]:
        Ans += num[max_idx + 1] + num[max_idx]
        num.pop(max_idx + 1)
    else:
        Ans += num[max_idx - 1] + num[max_idx]
        num.pop(max_idx - 1)

print(Ans)
#=================================================

end_time = time.time()
print('time: ', end_time - start_time)

'''
< 로직 >
1. 인접한 수 중 가장 큰 값에 병합되어야 함.
    - 그래야 큰 값이 더 많이 더해진다.

2. 자기 자신을 기준으로 양쪽 값 중 더 큰 값에 병합.

3. 풀이
    - max()을 통해 가장 큰 값을 찾는다.
    -> 가장 큰 값과 그 양쪽 값 중 작은 값과 누적합을 통해 답을 구한다.
    -> max()을 통해 찾은 값은 pop을 통해 index를 기반으로 제거한다.
    -> 리스트의 크기가 1이 되면 끝.
'''

'''
< 시간 복잡도 >
- 찾고 제거하고를 반복하기에 O(N)이 된다.
'''

'''
< 문제 정리 >
1. 순서가 정해진 여러 장의 카드 

2. 각각의 카드에는 레벨이 있음.

3. 조건
    - 두 카드는 인접한 카드여야 함.
    - 업그레이드 된 카드 A의 레벨은 변하지 않음.

4. 카드 합성시마다 두 카드 레벨의 합만큼 골드를 받음.

5. 최대한 많은 골드를 받도록하는 로직.
'''
```