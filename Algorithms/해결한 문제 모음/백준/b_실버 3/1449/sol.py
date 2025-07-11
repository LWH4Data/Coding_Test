import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#=============================================
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    nums = list(map(int, input().split()))
    
    # 물이 새는 위치를 연속하도록 정렬
    nums.sort()

    # 데이프의 개수를 카운트
    # 첫 번째 테이프는 무조건 사용.
    cnt = 1
    # 첫 번째 물이 새는 위치를 반환
    pos = nums[0]

    # 전체 리스트를 순회하면서 현재 위치보다 L보다 큰 값을 만나면 새로운 테이프를 사용해야한다.
    for i in range(1, N):
        if nums[i] >= pos + L:
            cnt += 1

            # 테이프의 시작 위치를 업데이트
            pos = nums[i]

    print(cnt)
#=============================================

end_time = time.time()
print(end_time - start_time)