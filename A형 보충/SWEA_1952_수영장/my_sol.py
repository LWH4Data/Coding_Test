import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#======================================================
T = int(input())

for tc in range(1, T + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))

#======================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >

'''

'''
< 시간 복잡도 >

'''

'''
< 문제 정리 >
1. 1년동안 + 각 달의 이용 계획 + 최소 비용

2. 이용권 네 종류
    - 1일
    - 1달
    - 3달
        - 11, 12월도 가능.
        - 
    - 1년
'''