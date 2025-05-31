import sys, time
sys.stdin = open('input_2720.txt')
start_time = time.time()

#===========================================================
# 금전 리스트 생성
costs = [25, 10, 5, 1]

# 거스름돈 반환 함수
def div(N):
    for cost in costs:
        N_a = N // cost
        N = N % cost

        if cost == 0.01 and N != 0:
            ans.append(int(N_a + 1))
        else:
            ans.append(int(N_a))

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ans = []

    # 함수로 답 구현
    div(N)
    print(*ans)
#===========================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
- 가장 큰 금액부터 거스름 돈을 주면 최소 돈전의 수로 반환할 수 있음.
'''

'''
< 문제 정의 >
- 거스름돈의 액수가 주어지면
    - 쿼터: 0.25
    - 다임: 0.1
    - 니켈: 0.05
    - 페니: 0.01

- 거스름 돈은 항상 5$ 이하

- 손님이 받는 동전의 개수 최소
'''

'''
< 시간 복잡도 >
- 최대 5원 이기 때문에 시간 복잡도는 O(N / 0.01)로 완탐 가능.
'''