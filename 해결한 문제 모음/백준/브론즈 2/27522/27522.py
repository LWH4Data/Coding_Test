import sys, time
sys.stdin = open('input_27522.txt')
start_time = time.time()

#================================================
from collections import defaultdict

# key와 val 따로 받기
key_temp = []
val_temp = []

for i in range(8):
    key, val = input().split()
    key_temp.append(key)
    val_temp.append(val)

# 시간에서 ':'을 제거하고 다시 구현
keys = []
for j in range(8):
    temp = ''
    cur_time = key_temp[j]
    for k in range(8):
        if cur_time[k] == ':':
            continue
        
        temp += cur_time[k]
    keys.append(temp)

# dict 구현
cars = defaultdict(list)
for c in range(8):
    cars[keys[c]].append(val_temp[c])

cars_1 = sorted(cars)

ans = []
for a in range(8):
    ans.append(cars[cars_1[a]])

        



#================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
1. dict로 구현? { 시간 : 팀 }

2. key에서 ':'없이 연결하고 sort

3. sort 기반으로 value를 비교하면서 각 Blue와 Red에 += 연산

4. 마지막에 비교해서 정답 출력
    4-1. 만약 같다면 가장 빠른 선수를 찾고 value를 반환.
'''

'''
< 시간 복잡도 >
- 계산할 정도로 크지 않다.

1. 시간의 전체 길이가 8임. 팀 합쳐도 9
'''

'''
< 문제 정리 >
1. 스피드전 승리 팀을 구하기.
    - 레드 팀 4명 + 블루 팀 4명 = 8 명

2. 각 팀원의 순위 점수의 합계가 높은 팀이 승리.
    - 순위가 같다면 최고 순위가 높은 쪽이 승리.

3. 리타이어 없음.

4. 모든 레이서가 반드시 다른 시간에 완주.

5. 
'''