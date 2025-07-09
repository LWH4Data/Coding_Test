import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#=============================================
T = int(input())

# 필요한 함수 정의
def find_S(A, B):
    # 연산 결과를 받을 변수 초기화.
    S = 0

    # 연산 수행.
    for _ in range(N):
        
        # 개별 항의 연산 수행.
        S += min(A) * max(B)

        # 연산에 사용된 원소 제거.
        A.pop(A.index(min(A)))
        B.pop(B.index(max(B)))
    
    # 결과 반환
    print(S)


for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 함수 실행
    find_S(A, B)
#=============================================

end_time = time.time()
print('time: ', end_time - start_time)

'''
< 로직 >
- 곱셈이기 때문에 가장 큰 B의 값에 가장 작은 A가 곱해져야 한다. 
- 위의 로직이 최적해를 보장하기에 greedy 문제이다.
- A의 최소를 min()으로, B의 최대를 max()로 추출하여 곱하고, 리스트에서 제외한다.
- 위의 과정을 반복하면 S의 최소값을 찾을 수 있다.
'''

'''
< 시간 복잡도 >
- max()와 min()을 통해 값을 반복적을 찾기에 O(N^2)이 된다. (나머지는 상수).
'''

'''
< 문제 정리 >

'''