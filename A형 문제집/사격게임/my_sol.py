import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#================================================
def cal(idx, data):
    if idx == 0:
        return data[1]
    
    elif idx == len(data):
        return data[-1]

    else:
        return data[idx - 1] * data[idx + 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    data_c = data.copy()
    flag = 0

    # while로 전체 탐색
    while flag != len(data):
        pass




#================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >

'''

'''
< 시간 복잡도 >
- 완전 탐색을 하는 경우 최대 10 개의 풍선을 순차적으로 터뜨리니까
    -> O(10!) 완탐 가능.

'''

'''
< 문제 정의 >
1. N 개의 풍선이 나란히 
    - 리스트?

2. 손님 = 게임 총 + N 개의 총알
    - N 번 사격

3. 터지고 난 뒤 터지지 않은 풍선들 재정렬

4. 점수 계산
    - 터진 풍선 기준 '좌 * 우'
    - 좌, 우 중 한 쪽만 있는 경우 해당 쪽의 점수만 get
    - 좌, 우 둘 다 없는 경우 터뜨린 풍선의 점수만 get
    - 터뜨린 풍선이 없는 경우 점수 X

5. 최대 점수

6. 변수 정리 
    - N: 1 ~ 10
    - K_i: 풍선에 적힌 수 1 ~ 1000
'''