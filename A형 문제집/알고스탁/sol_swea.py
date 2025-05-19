import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#=======================================================
T = int(input())
for tc in range(1,T+1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ms = Ms  # 코드 수정하기 힘들어서 원금 따로 저장
  
    for i in range(L+1):
        if i != 0:  # 0개월이 아닌 경우
            Ms += Ma  # 불입금액 추가
  
        check_arr = []  # 수익 발생하는 경우만 담는 것
        count = [0] * N
        if i != L: # 마지막 달이 아닌 경우
            for j in range(N):  # 종목수 만큼 반복하여 진행
                if arr[j][i] < arr[j][i+1]:  # 수익 발생하는 경우
                    profit = (arr[j][i+1]-arr[j][i]) / arr[j][i+1]
                    check_arr.append([profit, j])
                    check_arr.sort(reverse=True)  # 수익이 제일 큰 것부터 정렬
  
            for j in range(len(check_arr)):  # 매수 과정
                while Ms >= arr[check_arr[j][1]][i]:
                    Ms -= arr[check_arr[j][1]][i]
                    count[check_arr[j][1]] += 1
  
            for j in range(N):  # 매도 과정
                Ms += count[j]*arr[j][i+1]
  
    ans = Ms-ms-Ma*L  # 수익만 계산
    print(f'#{tc} {ans}')
#=======================================================

end_time = time.time()
print('time :', end_time - start_time)