import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#============================================
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    # 그리디를 위한 최대 수익 변수 초기화
    max_price = 0

    # 현재 수익 변수 초기화
    profit = 0

    # 역순으로 순회
    for i in range(N - 1, -1, -1):

        # 현재 가격이 max_price보다 크다면 max_price를 초기화
        if prices[i] > max_price:
            max_price = prices[i]

         # 크기 않다면 해당 날의 가격을 최대 가격에서 차감하고 더한다.
        else:
             profit += max_price - prices[i]
    
    print(profit)
#============================================

end_time = time.time()
print('time :', end_time - start_time )