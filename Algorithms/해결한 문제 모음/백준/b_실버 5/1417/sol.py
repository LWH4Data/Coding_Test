import sys, time
sys.stdin = open('input_1417.txt')
start_time = time.time()

#======================================================
import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dasom = int(input())
    others = []

    # 후보가 한 명인 경우 0을 출력.
    if N == 1:
        print(0)

        # 0출력 후 이후 코드는 실행되면 안 되기 때문에 skip
        continue

    for _ in range(N - 1):
        # heapq를 자료구조를 사용.
        # others에 각 후보의 지지자들을 push하는데 음수로 두어 최대힙 처럼 작동하도록 함.
        heapq.heappush(others, -int(input()))

    cnt = 0

    while others:
        # 최대 지지자 수를 반환
        max_vote = -heapq.heappop(others)

        # 다솜이가 최대지지자인 경우 종료
        if dasom > max_vote:
            break

        # 아닌 경우 한 명씩 매수하고, cnt 기록
        dasom += 1
        max_vote -= 1
        count += 1

        heapq.heappush(others, -max_vote)

    # 정답 출력.
    print(count)
#======================================================

end_time = time.time()
print('time :', end_time - start_time)