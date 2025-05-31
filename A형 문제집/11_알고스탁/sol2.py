import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#=====================================================
def solve(Ms, Ma, N, L, prices):
    memo = {}

    def dfs(month, cash, holdings):
        key = (month, cash, tuple(holdings))
        if key in memo:
            return memo[key]

        if month == L:
            return cash + sum(holdings[i] * prices[i][month] for i in range(N))

        # 월 시작: 불입금 수령 (매도/매수 전에 한 번만)
        cash += Ma
        res = 0

        # 1. 보유 주식 전량 매도
        sell_cash = cash + sum(holdings[i] * prices[i][month] for i in range(N))
        res = max(res, dfs(month + 1, sell_cash, [0] * N))

        # 2. 아무것도 안 하기
        res = max(res, dfs(month + 1, cash, holdings[:]))

        # 3. 복합 매수 조합 완전 탐색
        def buy_combo(idx, remain_cash, new_holdings):
            if idx == N:
                res_case = dfs(month + 1, remain_cash, new_holdings)
                nonlocal res
                res = max(res, res_case)
                return

            price = prices[idx][month]
            max_cnt = remain_cash // price
            for cnt in range(max_cnt + 1):
                new_holdings[idx] += cnt
                buy_combo(idx + 1, remain_cash - cnt * price, new_holdings)
                new_holdings[idx] -= cnt

        buy_combo(0, cash, holdings[:])

        memo[key] = res
        return res

    final = dfs(0, Ms, [0] * N)
    return final - (Ms + Ma * L)


T = int(input())
for tc in range(1, T + 1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    prices = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {solve(Ms, Ma, N, L, prices)}")
#=====================================================

end_time = time.time()
print('time :', end_time - start_time)