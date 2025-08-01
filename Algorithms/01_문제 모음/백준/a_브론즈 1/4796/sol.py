import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#==========================================================================
flag = True
tc = 0
while flag:
    L, P, V = map(int, input().split())
    Ans = 0
    tc += 1
    temp = 0

    # L, P, V가 모두 0인 경우 반복문을 중단하는 영역.
    if (L, P, V) == (0, 0, 0):
        flag = False
    
    # python에서 중간 중단을 위해서는 이렇게 flag를 사용해 주어야 함.
    if flag == False:
        break

    # 첫 번째 해를 구하기.
    first = V // P

    # 나머지 받아두기
    days_last = V % P


    # 첫 번째 일 수 연산
    Ans = first  * L
    
    # 나머지 연산
    if L >= days_last:
        Ans += days_last
    else:
        Ans += L

    print(f'Case {tc}: {Ans}')
#==========================================================================

end_time = time.time()
print('time: ', end_time - start_time)

'''
< 로직 >
1. 강산이의 휴가(V)를 연속하는 일 수(P)로 나눈 몫을 찾는다.

2. 연속하는 일 수(P)를 사용 가능 일 수(L)로 나눈 몫을 찾는다. 

3. 1과 2에서 찾은 몫들을 곱하면 최대 일 수를 알 수 있다.

4. 단, 몫을 구하고 남은 나머지 또한 count를 해 주어야 한다.
    - 나머지보다 L이 크다면 나머지를 더하고
    - 나머지가 L보다 크다면 나머지를 더한다.
'''

'''
< 시간 복잡도 >
- 상수 연산.
'''

'''
< 문제 정리 >
1. 연속하는 P일 중 L일만 사용 가능. 강산이는 V일짜리 휴가 시작.

2. 강산이가 캠핑장을 이용할 수 있는 최대 일 수.

3. L, P, V 순으로 입력됨.
'''