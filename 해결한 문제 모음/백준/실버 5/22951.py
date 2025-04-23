import sys, time
sys.stdin = open('input_22951.txt')
start_time = time.time()

#==============================================
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    

#==============================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 문제 정리 >
1. N명이 둥글게, k 개의 카드

2. 혜민이부터 반시계방향으로 1 ~ N의 번호가 주어짐.

3. 카드에는 1 <= 수 <= 10 정수

4. N x K개의 카드 배치(순서 X)

5. 1번 사람의 제일 왼쪽 카드에서 시작
    5-1. 카드에 적힌 수 X를 확인 및 제거
    5-2. 제거된 카드의 반시계방향으로 X 번째 위치한 카드 선택

6. 마지막 한 장이 남으면 해당 인원이 승리.



'''