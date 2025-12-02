"""
< deque 슬라이딩 윈도우>
● 이중 리스트는 안되나?
  → deque는 앞·뒤 삭제가 O(1)이고, 
    리스트는 앞 삭제가 O(N)이라서 시간 복잡도가 폭발한다.
  → 리스트 앞을 지우면 공간을 메우기 위해 O(N)의 이동이 발생.
● 이중 리스트와 인덱스를 통해 구현 가능할듯?
"""

import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=========================================
# 입력값 받기
N, L = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
ans = []

# 슬라이딩 윈도우의 두 지점.
end = 0
start = end - L + 1
temp = float('inf')

# 알고리즘 시작
while end != N:

    # end > 0 인데 start < 0인 경우.
    if start < 0:
        temp = min(numbers[0 : end + 1])
        ans.append(temp)
        end += 1
        start = end - L  + 1
        continue

    # 둘 다 아닌 경우.
    numbers_sorted = sorted(numbers[start : end + 1])
    temp = numbers_sorted[0]
    ans.append(temp)
    end += 1
    start = end - L  + 1

print(*ans)
#=========================================

end = time.time()
print("time:", start - end)