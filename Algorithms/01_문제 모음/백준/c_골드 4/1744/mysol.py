import sys, heapq
sys.stdin = open("input.txt")

# 입력 받기
N = int(sys.stdin.readline().strip())
numbers = []
for _ in range(N):
    heapq.heappush(numbers, int(sys.stdin.readline()))
ans = 0

# 리스트를 나뉘 위해 한 번 정렬
numbers.sort()

# 양수와 음수 + 0으로 두 개의 리스트로 나눈다.
for i in range(len(numbers)):
    if numbers[i] > 0:
        index = i
        break

num_pos = numbers[i : ]
num_neg = numbers[ : i]

while len(num_neg) >= 1:
    if len(num_neg) == 1:
        ans += num_neg[0]
        break

    data1 = heapq.heappop(num_neg)
    data2 = heapq.heappop(num_neg)

    ans += (data1 * data2)

while len(num_pos) >= 1:
    if len(num_pos) == 1:
        ans += num_pos[0]
        break

    data1 = heapq.heappop(num_pos)
    data2 = heapq.heappop(num_pos)

    if data1 == 1 and num_pos:
        ans += 1
        if num_pos:
            data1 = heapq.heappop(num_pos)

    if data2 == 1:
        ans += 1
        if num_pos:
            data2 = heapq.heappop(num_pos)
    
    ans += (data1 * data2)

print(ans)