"""
< 문제 정리 >
● 시간 복잡도: nlogn(정렬) + n^2/2(투 포인터 탐색) = O(N^2)
● 예외 처리할 부분이 많았다...
"""

import sys, time
sys.stdin = open("input.txt")
start = time.time()

#==========================================
# 입력 받기
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
ans = 0
flag = 0

# 정렬 하기
numbers = sorted(numbers)

# 반복
while flag != len(numbers):
   
    # 탐색할 수를 저장.
    temp = numbers[flag]

    # 투 포인터 지정.
    left = 0
    right = len(numbers) - 1
    
    # 탐색 시작
    while left != right:
        
        if left == flag:
            left += 1
            # 만약 두 위치가 같다면 flag += 1
            if right == left:
                flag += 1
            continue
        
        elif right == flag:
            right -= 1
            # 만약 두 위치가 같다면 flag += 1
            if right == left:
                flag += 1
            continue
        
        # 두 수의 합이 찾던 수와 같다면 증가
        elif numbers[left] + numbers[right] == temp:
            ans += 1
            flag += 1
            break

        # 합이 더 크다면 오른쪽 포인터 차감
        elif numbers[left] + numbers[right] > temp:
            right -= 1
            
            # 만약 두 위치가 같다면 flag += 1
            if right == left:
                flag += 1
        
        # 합이 더 작다면 왼쪽 포이터 증가.
        elif numbers[left] + numbers[right] < temp:
            left += 1

            # 만약 두 위치가 같다면 flag += 1
            if right == left:
                flag += 1
        
print(ans)
#==========================================

end = time.time()
print("time:", end - start)