import sys, time
sys.stdin = open('input.txt')
start_time =time.time()

#=============================================
T = int(input())

# 연속하지 않은 quack의 수를 세는 함수
def find_quack():
    # 찾는 단어 quack의 몇 번째 글자를 탐색 중인지 확인하는 index
    idx = 0
    # 최소 하나의 quack이라도 찾았는지 확인하는 변수
    found = False
    
    # 전체를 탐색
    for i in range(len(sound)):
        
        # 방문 했다면 pass
        if visited[i]:
            continue

        # 소리와 탐색하는 글자가 같ㄷ면 방문체크 후 다음으로 진행
        if sound[i] == order[idx]:
            visited[i] = True
            idx += 1

            # 만약 idx==5인 경우 글자 하나가 완성
            if idx == 5:
                # idx 초기화하여 새로 탐색 시작
                idx = 0
                # 최소 한 마리를 찾았기에 found 변수 변경
                found = True

for tc in range(1, T + 1):
    sound = input()
    order = 'quack' # 탐색할 문자열 초기화
    visited = [False] * len(sound) # 연속하지 않은 경우를 찾기에 방문 체크 필요.
    answer = 0 # 정답 변수 초기화

    # find_duct()이 성공한 횟수가 총 quack의 수이기에 answer에 누적합
    # find_duct() 함수는 한 번 수행될 때 한 개의 quack을 찾는다.
    while find_quack():
        answer += 1

    # 방문한 글자이거나(visited = True) sound가 order에 속하지 않는다면 -1을 춢력
    if all(visited[i] or sound[i] not in order for i in range(len(sound))):
        print(-1)
    # 위의 경우가 아니라면 quack이 count된 것이기에 정답 출력
    else:
        print(answer)
#=============================================

end_time = time.time()
print('time :', end_time - start_time)