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