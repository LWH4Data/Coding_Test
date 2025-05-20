import sys
sys.stdin = open('sample_in.txt')

# 최대 수익 저장용 변수
max_profit = 0

def dfs(month, cash, holdings):
    global max_profit

    if month == L:
        total_value = cash
        for i in range(N):
            total_value += holdings[i] * prices[i][month]
        max_profit = max(max_profit, total_value)
        return

    # 1. 불입금액 추가
    cash += Ma

    # 2. 아무것도 안 하기
    dfs(month + 1, cash, holdings[:])

    # 3. 현재 보유 주식 전부 매도
    temp_cash = cash
    for i in range(N):
        temp_cash += holdings[i] * prices[i][month]
    dfs(month + 1, temp_cash, [0] * N)

    # 4. 주식 사기 (모든 가능한 조합 - 완탐)
    def buy_stocks(i, cur_cash, cur_holdings):
        if i == N:
            dfs(month + 1, cur_cash, cur_holdings)
            return

        price = prices[i][month]
        max_qty = cur_cash // price

        for q in range(max_qty + 1):
            cur_holdings[i] += q
            buy_stocks(i + 1, cur_cash - price * q, cur_holdings)
            cur_holdings[i] -= q

    buy_stocks(0, cash, holdings[:])


# ================================
T = int(input())
for tc in range(1, T + 1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    prices = [list(map(int, input().split())) for _ in range(N)]

    max_profit = 0
    dfs(0, Ms, [0] * N)
    total_invested = Ms + Ma * L
    print(f"#{tc} {max_profit - total_invested}")
