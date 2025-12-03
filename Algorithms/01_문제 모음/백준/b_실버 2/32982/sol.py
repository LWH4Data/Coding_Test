import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#===============================================================
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A0, A1, B0, B1, C0, C1 = map(int, input().split())

    ok = True
    cur = 0  # 첫 복용 시간은 아직 정하지 않음

    # 첫 번째 복용: 아침 시간 중에서 가능한 earliest 복용 시점 계산
    t_min = max(A0, B0 - K)
    if t_min > A1:
        ok = False
    else:
        cur = min(B1, t_min + K)

    # N일 동안 반복
    for day in range(1, N + 1):
        if not ok:
            break

        # 점심 → 저녁
        t_min = max(cur, C0 - K)
        if t_min > B1:
            ok = False
            break
        cur = t_min + K

        # 저녁 → 다음 날 아침
        if day < N:
            t_min = max(cur, A0 + 1440 - K)
            if t_min > C1:
                ok = False
                break
            cur = min(A1 + 1440, t_min + K) - 1440  # 다음날 아침 기준으로 맞추기

    print("YES" if ok else "NO")
#===============================================================

end_time = time.time()
print('time :', end_time - start_time)
