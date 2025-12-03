import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#===============================================================
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A0, A1, B0, B1, C0, C1 = map(int, input().split())

    flag = True
    cur = 0  # 첫 복용 시간은 아직 정하지 않음

    # 한 번이라도 범위를 벗어나면 안됨. 벗어나면 다음 테스트 케이스.
    if A0 - K + 1440 > C1 or B0 - K > A1 or C0 - K > B1:
        print("No")
        continue

    # 위의 경우가 아닌 경우 초기값은 B0 - K
    else: 
        cur = B0 - K

    # N일 동안 반복
    for day in range(1, N + 1):

        if cur + K < B0:
            print("No")
            flag = False
            break
        else:
            cur = max(cur + K, B1)

        if cur + K < C0:
            print("No")
            flag = False
            break
        else:
            cur = max(cur + K, C1)

        if cur + K - 1440 < A0:
            print("No")
            flag = False
            break
        else:
            cur = max(cur + K, A1)

    if flag:
        print("Yes")
#===============================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 >
1. 각 식사간의 차이가 가장 크도록 한다.
    - 이때 두 식사간의 차이가 K보다 큰 경우 No를 출력한다.
'''

'''
< 시간 복잡도 >
- N일간만 비교하면 되기에 O(N)이 된다.
'''

'''
< 문제 정리 >
1. N일치 감기약.

2. 하루 세 번, 식후 바로 복용, 지속 시간은 K 분.

4. 약효과 끊이지 않게 유지.
'''