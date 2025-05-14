import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#======================================================
def DFS(comb=[]):
    if len(comb) == K:
        '''
        < (''.join(comb)) >
        1. 문자열을 합친다.
            - '': 구분자 없이
            - join(comb): comb의 요소들을 합친다.
        '''
        result.add(''.join(comb))  # 문자열로 이어붙여 set에 추가
        return

    for i in range(N):
        if visited[i]:
            continue  # 방문했으면 스킵 (중복 방지)

        visited[i] = True
        DFS(comb + [arr[i]])
        visited[i] = False

# 테스트 케이스 수
T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 카드 수
    K = int(input())  # 선택할 카드 수
    '''
    < input().strip() >
    1. 자료를 양쪽 공백을 제거(strip())하여 문자열로 반환한다.
    '''
    arr = [input().strip() for _ in range(N)]  # 카드 숫자 (문자열)
    visited = [False] * N
    result = set()  # 중복 제거용 set

    DFS()
    print(len(result))
#======================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 시간 복잡도 >
- 순열의 시간 복잡도
    -> O(N! / (N - k)!)

- 단, 백트래킹으로 인하여 최악의 경우로 가는 경우는 거의 없다.
'''

'''
< 문제 정의 >
- 조합을 DFS로 구현하는 단순한 백트래킹 문제.
'''