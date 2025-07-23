import sys, time
sys.stdin = open('input_14729.txt')
start_time = time.time()

#=========================================================
def sol():

    # 완전 탐색
    a = 0
    for i in range(len(milks)):

        # 첫 딸기우유 추가.
        if not ans and milks[i] == 0:
            ans.append(milks[i])
            a = i + 1
            break
    
    for i in range(a, len(milks)):

        # 초코 우유
        if ans[-1] == 0 and milks[i] == 1:
            ans.append(milks[i])

        # 바나나
        if ans[-1] == 1 and milks[i] == 2:
            ans.append(milks[i])
        
        # 다시 딸기
        if ans[-1] == 2 and milks[i] == 0:
            ans.append(milks[i])
        
N = int(input())
milks = list(map(int, input().split()))
ans = []

sol()
print(len(ans))
#=========================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >
- 마시는 경우

- 마시지 않는 경우

- 전체 우유 개수 cnt
'''

'''
< 시간 복잡도 >
- 완탐은 O(N)

- N이 1,000이기에 완탐 가능.
'''

'''
< 문제 정의 >
- 딸, 바, 초

- 처음에는 딸기 우유
    -> 다음 초코
    -> 다음 바나나
    -> 다음 딸기

- 각 가게는 딸, 초, 바 중 하나만을 취급

- 우유를 사마시거나 마시지 않음.
'''