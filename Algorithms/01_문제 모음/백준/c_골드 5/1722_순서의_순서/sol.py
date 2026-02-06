import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

# 3개를 선택하는 완탐시 20 * 20 * 20으로 가능할 듯. 여기에 정렬 Nlog(N)
#==============================================================
F = [0] * 21
S = [0] * 21
visited = [False] * 21
N = int(sys.stdin.readline())
F[0] = 1

# 팩토리얼 리스트 초기화
for i in range(1, N + 1):
    F[i] = F[i - 1] * i

# list로 입력 받기
num_list = list(map(int, sys.stdin.readline().split()))

# 1인 경우 K번째 순열 찾기
if num_list[0] == 1:

    # K 초기화
    K = num_list[1]

    # i번째 자리에 들어갈 숫자를 찾기
    for i in range(1, N + 1):
        cnt = 1  # 남은 숫자들 중 몇 번째를 선택할지 (1부터 시작)

        # 1부터 N까지 모든 숫자를 확인
        for j in range(1, N + 1):
            # 숫자 j를 이미 사용했다면 건너뛰기
            if visited[j]:
                continue

            # K가 cnt * F[N-i] 이하이면, 남은 숫자 중 cnt번째 숫자가 답
            if K <= cnt * F[N - i]:
                # 이전 그룹들의 경우의 수를 K에서 빼고
                K -= F[N - i] * (cnt - 1)
                # i번째 자리에 숫자 j를 배치
                S[i] = j
                visited[j] = True
                break
            
            # 아직 K가 더 크면, 다음 숫자 그룹으로
            cnt += 1
    
    for i in range(1, N + 1):
        print(S[i], end=' ')

else:
    # 주어진 순열이 몇 번째인지 구하기 (K = 1부터 시작)
    K = 1
    
    # 각 자리를 순회하며 앞에 몇 개의 순열이 있는지 계산
    for i in range(1, N + 1):
        cnt = 0  # num_list[i]보다 작으면서 아직 안 쓴 숫자 개수

        # num_list[i]보다 작은 숫자들 중 미사용 숫자를 세기
        for j in range(1, num_list[i]):
            if not visited[j]:
                cnt += 1
        
        # cnt개의 작은 숫자로 시작하는 순열들을 모두 건너뜀
        #  ● cnt: 현재 선택한 수보다 작은 미사용 수의 개수
        #  ● F[N - i]: 현재 자리 이후 남은 자리들의 경우의 수
        K += cnt * F[N - i]
        
        # 현재 자리의 숫자를 사용했다고 표시
        visited[num_list[i]] = True
    print(K)
#==============================================================

e_t = time.time()
print("time: ", e_t - s_t)